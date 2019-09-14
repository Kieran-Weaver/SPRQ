import json
import collections
import threading
DEBUG = 1
#PlayerState is dynamic data, the saved json is static data
class PlayerState:
	hp = 100
	sp = 100
	xp = 0
	money = 0
	location = 'UTP Lounge'
	items = {}
	status = {}

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
			json.dump(self.savedData,f)
			
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
		self.players[playerid] = PlayerState()
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

	def printRoom(self,playerid):
		room = self.savedData['rooms'][self.players[playerid].location]
		rmessage = [room['name'],room['info'],'Items:'] + room['items']
#		rmessage = rmessage + ['People Here:'] + rooms['players']
		rmessage.append('Region: ' + room['region'])
		self.writeMessage("\n".join(rmessage))
		
	def killPlayer(self,playerid):
		room = self.savedData['rooms'][self.players[playerid].location]
		for key in self.players[playerid].items:
			for i in range(self.players[playerid].items[key]):
				self.savedData['rooms'][room['name']]['items'].append(key)
		self.players[playerid].items = {}
		self.players[playerid].location = self.savedData['respawn'][room['region']]['room']
		self.writeMessage(self.savedData['respawn'][room['region']]['message'])

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
		if (messagelist[0] == "ride"):
			messagelist.pop(0)
			self.fastTravel(playerid,message[5:])
		elif (messagelist[0][:4] == 'inv'):
			self.printInventory(playerid)
		elif (messagelist[0] == "panic"):
			self.killPlayer(playerid)
		else:
			self.movePlayer(playerid,message)
