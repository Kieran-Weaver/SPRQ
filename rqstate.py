import json
import collections
import threading
import time
DEBUG = 1
#PlayerState is dynamic data, the saved json is static data
healCost = 20
attackCost = 0
blockCost = 5
class PlayerState:
	hp = 100 # Goes down over time in battle
	sp = 100 # For using "attack", "block", and "heal"
	maxHP = 100
	atk = 4
	xp = 0
	money = 0
	location = 'UTP Lounge'
	items = {}
	state = "map"
	status = {"battle" : {}}

class RQState:
	savedData = {}
	players = {}
	inqueue = collections.deque()
	iqlock = threading.Lock()
	outqueue = collections.deque()
	oqlock = threading.Lock()
	def __init__(self,filename):
		with open(filename,"r") as f:
			self.savedData = json.load(f)
		for player in self.savedData['players']:
			self.loadPlayer(player)
			
	def savestate(self,filename):
		for player in self.players:
			self.savePlayer(player)
		with open(filename,"w") as f:
			json.dump(self.savedData,f,indent=2)
			
	def writeMessage(self,message):
		self.oqlock.acquire()
		self.outqueue.append(message)
		self.oqlock.release()
		
	def createPlayer(self,playerid):
		self.players[playerid] = PlayerState()
		self.savedData['players'][playerid] = {}
		self.savedData['players'][playerid]['hp'] = 100
		self.savedData['players'][playerid]['sp'] = 100
		self.savedData['players'][playerid]['xp'] = 0
		self.savePlayer(playerid)
		
	def loadPlayer(self,playerid):
		self.players[playerid].hp = self.savedData['players'][playerid]['hp']
		self.players[playerid].sp = self.savedData['players'][playerid]['sp']
		self.players[playerid].xp = self.savedData['players'][playerid]['xp']
		self.players[playerid].location = self.savedData['players'][playerid]['location']
		self.players[playerid].money = self.savedData['players'][playerid]['money']
		self.players[playerid].items = self.savedData['players'][playerid]['items']
		
	def savePlayer(self,playerid):
		self.savedData['players'][playerid]['items'] = self.players[playerid].items
		self.savedData['players'][playerid]['xp'] = self.players[playerid].xp
		self.savedData['players'][playerid]['money'] = self.players[playerid].money
		self.savedData['players'][playerid]['location'] = self.players[playerid].location
		
	def movePlayer(self,playerid, exitname):
		directions = ["north","south","east","west","n","s","e","w"]
		if (exitname in directions):
			exitindex = directions.index(exitname) % 4
			if (self.savedData['rooms'][self.players[playerid].location]['exits'][exitindex] == "none"):
				self.writeMessage("That is not an exit")
				return
			else:
				self.players[playerid].location = self.savedData['rooms'][self.players[playerid].location]['exits'][exitindex]
		elif exitname in self.savedData['rooms'][self.players[playerid].location]['exits']:
			self.players[playerid].location = exitname
		else:
			self.writeMessage("That is not an exit")

	def handleRoom(self, playerid):
		room = self.savedData['rooms'][self.players[playerid].location]
		if (room["npcs"]):
			self.players[playerid].status["battle"] = self.savedData["npcs"][room["npcs"][0]].copy()
			self.players[playerid].state = "battle"
			self.oqlock.acquire()
			self.outqueue.append(self.players[playerid].status["battle"]["text"]["entry"])
			self.oqlock.release()

	def handleBattle(self,playerid, message):
		messagelist = message.split()
		if ((messagelist[0] == "attack") and (self.players[playerid].sp >= attackCost)):
			self.players[playerid].status["battle"]["hp"] -= (self.players[playerid].atk - self.players[playerid].status["battle"]["def"])
			self.players[playerid].sp -= attackCost
		elif ((messagelist[0] == "heal") and (self.players[playerid].sp >= healCost)):
			self.players[playerid].hp = self.players[playerid].maxHP
			self.players[playerid].sp -= healCost
		if (self.players[playerid].status["battle"]["hp"] < 0):
			self.oqlock.acquire()
			self.outqueue.append(self.players[playerid].status["battle"]["text"]["win"])
			self.oqlock.release()
			self.players[playerid].status["battle"] = {}
			self.players[playerid].state = "map"
			self.players[playerid].sp = 100
			self.players[playerid].hp = self.players[playerid].maxHP
			return
		defMul = 1.0
		if ((messagelist[0] == "block") and (self.players[playerid].sp >= blockCost)):
			defMul = 0.5
			self.players[playerid].sp -= blockCost
		self.players[playerid].hp -= defMul*self.players[playerid].status["battle"]["atk"]
		self.oqlock.acquire()
		if (self.players[playerid].hp <= 0):
			self.outqueue.append(self.players[playerid].status["battle"]["text"]["lose"])
			self.oqlock.release()
			self.players[playerid].state = "map"
			self.killPlayer(playerid)
			return
		else:
			self.outqueue.append(self.players[playerid].status["battle"]["text"]["turn"])
			self.oqlock.release()
		self.printState(playerid)
		self.printNPC(playerid)
		
	def printRoom(self,playerid):
		room = self.savedData['rooms'][self.players[playerid].location]
		rmessage = [room['name'],room['info'],'Items:'] + room['items']
#		rmessage = rmessage + ['People Here:'] + rooms['players']
		rmessage.append('Region: ' + room['region'])
		self.writeMessage("\n".join(rmessage))
	
	def printNPC(self, playerid):
		self.oqlock.acquire()
		self.outqueue.append("NPC Name: " + self.players[playerid].status["battle"]["name"])
		self.outqueue.append("NPC HP: {}".format(self.players[playerid].status["battle"]["hp"]))
		self.oqlock.release()
		
	def killPlayer(self,playerid):
		room = self.savedData['rooms'][self.players[playerid].location]
		for key in self.players[playerid].items:
			for i in range(self.players[playerid].items[key]):
				self.savedData['rooms'][room['name']]['items'].append(key)
		self.players[playerid].items = {}
		self.players[playerid].location = self.savedData['respawn'][room['region']]['room']
		self.writeMessage(self.savedData['respawn'][room['region']]['message'])

	def printState(self, playerid):
		player = self.players[playerid]
		self.oqlock.acquire()
		self.outqueue.append("HP: {}".format(player.hp))
		self.outqueue.append("SP: {}".format(player.sp))
		self.oqlock.release()
		
	def printInventory(self,playerid):
		self.oqlock.acquire()
		self.outqueue.append("Money: {}".format(self.players[playerid].money))
		self.outqueue.append("Items: ")
		for key in self.players[playerid].items:
			self.outqueue.append(str(key))
			if (self.players[playerid].items[key] > 1):
				self.outqueue[-1] += ' x {}\n'.format(self.players[playerid].items[key])
		self.oqlock.release()
		
	def fastTravel(self,playerid,message):
		if (message in self.savedData['fast-travel']):
			stops = self.savedData['fast-travel'][message]
			if (self.players[playerid].location in stops):
				cost = 100
				if (message[5:16].lower() == "canada line"):
					cost = 200
				if (self.players[playerid].money < cost):
					self.writeMessage("Not enough money to ride")
				else:
					self.players[playerid].money -= cost
					self.players[playerid].location = message
			else:
				self.writeMessage("You cannot ride that here!")
		else:
			self.writeMessage("{} is not a route".format(message))
		
	def parseMessage(self,playerid,message):
		messagelist = message.split()
		if (DEBUG == 1):
			if (messagelist[0] == "modmove"):
				self.players[playerid].location = message[8:]
				return
			elif (messagelist[0] == "modmoney"):
				self.players[playerid].money += int(messagelist[1])
				return
		if (self.players[playerid].state == "map"):
			if (messagelist[0] == "ride"):
				messagelist.pop(0)
				self.fastTravel(playerid,message[5:])
			elif (messagelist[0][:4] == 'inv'):
				self.printInventory(playerid)
			elif (messagelist[0] == "panic"):
				self.killPlayer(playerid)
			else:
				self.movePlayer(playerid,message)
				self.handleRoom(playerid)
		elif (self.players[playerid].state == "battle"):
			if (messagelist[0][:4] == "inv"):
				self.printState(playerid)
				self.printInventory(playerid)
			else:
				self.handleBattle(playerid, message)
