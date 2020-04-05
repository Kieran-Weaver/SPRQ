import json
import collections
import queue
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
	battle = {}
	status = {}

class RQState:
	savedData = {}
	players = {}
	outqueue = queue.SimpleQueue()
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
		self.outqueue.put(message)

	def loadPlayer(self,playerid):
		self.players[playerid] = PlayerState()
		if not (playerid in self.savedData['players']):
			self.savePlayer(playerid)
		self.players[playerid].maxHP = self.savedData['players'][playerid]['hp']
		self.players[playerid].hp = self.players[playerid].maxHP
		self.players[playerid].sp = self.savedData['players'][playerid]['sp']
		self.players[playerid].xp = self.savedData['players'][playerid]['xp']
		self.players[playerid].atk = self.savedData['players'][playerid]['atk']
		self.players[playerid].location = self.savedData['players'][playerid]['location']
		self.players[playerid].money = self.savedData['players'][playerid]['money']
		self.players[playerid].items = self.savedData['players'][playerid]['items']
		return True
		
	def savePlayer(self,playerid):		
		self.savedData['players'][playerid] = {}
		self.savedData['players'][playerid]['hp'] = self.players[playerid].maxHP
		self.savedData['players'][playerid]['sp'] = self.players[playerid].sp
		self.savedData['players'][playerid]['xp'] = self.players[playerid].xp
		self.savedData['players'][playerid]['atk'] = self.players[playerid].atk
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
				return False
			else:
				self.players[playerid].location = self.savedData['rooms'][self.players[playerid].location]['exits'][exitindex]
		elif exitname in self.savedData['rooms'][self.players[playerid].location]['exits']:
			self.players[playerid].location = exitname
		else:
			self.writeMessage("That is not an exit")
			return False
		return True

	def handleRoom(self, playerid):
		room = self.savedData['rooms'][self.players[playerid].location]
		if (room["npcs"]):
			self.setState(playerid, "battle")
			self.writeMessage(self.players[playerid].battle["text"]["entry"])

	def handleBattle(self,playerid, message):
		messagelist = message.split()

		if ((messagelist[0] == "attack") and (self.players[playerid].sp >= attackCost)):
			self.players[playerid].battle["hp"] -= (self.players[playerid].atk - self.players[playerid].battle["def"])
			self.players[playerid].sp -= attackCost
		elif ((messagelist[0] == "heal") and (self.players[playerid].sp >= healCost)):
			self.players[playerid].hp = self.players[playerid].maxHP
			self.players[playerid].sp -= healCost

		if (self.players[playerid].battle["hp"] <= 0):
			self.outqueue.put(self.players[playerid].battle["text"]["win"])
			self.setState(playerid, "map")
			return
		defMul = 1.0
		if ((messagelist[0] == "block") and (self.players[playerid].sp >= blockCost)):
			defMul = 0.5
			self.players[playerid].sp -= blockCost
		self.players[playerid].hp -= round(defMul*self.players[playerid].battle["atk"]*(time.monotonic() - self.players[playerid].battle["time"]))
		if (self.players[playerid].hp <= 0):
			self.writeMessage(self.players[playerid].status["battle"]["text"]["lose"])
			self.killPlayer(playerid)
			return
		else:
			self.writeMessage(self.players[playerid].battle["text"]["turn"])
		self.players[playerid].battle['time'] = time.monotonic()
		
	def setState(self, playerid, state):
		if (state == "map"):
			self.players[playerid].battle = {}
			self.players[playerid].state = "map"
			self.players[playerid].sp = 100
			self.players[playerid].hp = self.players[playerid].maxHP
		elif (state == "battle"):
			room = self.savedData['rooms'][self.players[playerid].location]
			self.players[playerid].battle = self.savedData["npcs"][room["npcs"][0]].copy()
			self.players[playerid].battle['time'] = time.monotonic()
			self.players[playerid].state = "battle"
		else:
			if (DEBUG == 1):
				self.writeMessage("Invalid state: " + str(state))

	def killPlayer(self,playerid):
		room = self.savedData['rooms'][self.players[playerid].location]
		for key in self.players[playerid].items:
			for i in range(self.players[playerid].items[key]):
				self.savedData['rooms'][room['name']]['items'].append(key)
		self.players[playerid].items = {}
		self.players[playerid].location = self.savedData['respawn'][room['region']]['room']
		self.setState(playerid, "map")
		self.writeMessage(self.savedData['respawn'][room['region']]['message'])

	def printState(self, playerid):
		player = self.players[playerid]
		if (player.state == "map"):
			room = self.savedData['rooms'][self.players[playerid].location]
			rmessage = [room['name'],room['info'],'Items:'] + room['items']
#			rmessage = rmessage + ['People Here:'] + rooms['players']
			rmessage.append('Region: ' + room['region'])
			self.writeMessage("\n".join(rmessage))
		elif (player.state == "battle"):
			self.writeMessage("HP: {}".format(player.hp))
			self.writeMessage("SP: {}".format(player.sp))
			self.writeMessage("NPC Name: " + self.players[playerid].battle["name"])
			self.writeMessage("NPC HP: {}".format(self.players[playerid].battle["hp"]))
		
	def printInventory(self,playerid):
		self.writeMessage("Money: {}".format(self.players[playerid].money))
		self.writeMessage("Items: ")
		for key in self.players[playerid].items:
			keystr = str(key);
			if (self.players[playerid].items[key] > 1):
				keystr += ' x {}\n'.format(self.players[playerid].items[key])
			self.writeMessage(keystr)
		
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
			elif self.movePlayer(playerid,message):
				self.handleRoom(playerid)
		elif (self.players[playerid].state == "battle"):
			if (messagelist[0][:4] == "inv"):
				self.printState(playerid)
				self.printInventory(playerid)
			else:
				self.handleBattle(playerid, message)
