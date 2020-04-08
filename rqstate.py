import json
import collections
import queue
import threading
import time
import random
DEBUG = 1
#PlayerState is dynamic data, the saved json is static data
healCost = 20
attackCost = 0
blockCost = 5
class PlayerState:
	hp = 100 # Goes down over time in battle
	sp = 100 # For using "attack", "block", and "heal"
	maxHP = 100
	itemCapacity = 10
	atk = 4
	xp = 0
	money = 0
	location = 'UTP Lounge'
	items = {}
	state = "map"
	battle = {}
	powerups = set()
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

	def numItems(self, playerid):
		items = [item for item in self.players[playerid].items]
		return sum([self.players[playerid].items[item] for item in items])
	
	def addItem(self, playerid, item):
		if self.numItems(playerid) < self.players[playerid].itemCapacity:
			if item in self.players[playerid].items.keys():
				self.players[playerid].items[item] += 1
			else:
				self.players[playerid].items[item] = 1
			return True
		else:
			self.writeMessage("You cannot pick up any more items!")
			return False
	
	def removeItem(self, playerid, item):
		if item in self.players[playerid].items.keys():
			self.players[playerid].items[item] -= 1
			if self.players[playerid].items[item] == 0:
				del self.players[playerid].items[item]
			return True
		else:
			return False

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
		self.players[playerid].itemCapacity = self.savedData['players'][playerid]['itemCapacity']
		self.players[playerid].powerups = self.savedData['players'][playerid]['powerups']
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
		self.savedData['players'][playerid]['itemCapacity'] = self.players[playerid].itemCapacity
		self.savedData['players'][playerid]['powerups'] = self.players[playerid].powerups
		
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

	def damageNPC(self, playerid, atk):
		if self.players[playerid].state == "battle":
			self.players[playerid].battle["hp"] -= max(atk - self.players[playerid].battle["def"], 0)
		else:
			self.writeMessage("There is nothing to attack")

	def checkWin(self, playerid):
		if (self.players[playerid].state == "battle") and (self.players[playerid].battle["hp"] <= 0):
			self.outqueue.put(self.players[playerid].battle["text"]["win"])
			self.players[playerid].money += self.players[playerid].battle["money"]
			for item in self.players[playerid].battle["drops"]:
				if (random.randrange(0, 256) <= self.players[playerid].battle["drops"][item]):
					self.addItem(playerid, item)
			self.setState(playerid, "map")
			return True
		else:
			return False
		
	def handleBattle(self,playerid, message):
		messagelist = message.split()

		if ((messagelist[0] == "attack") and (self.players[playerid].sp >= attackCost)):
			self.damageNPC(playerid, self.players[playerid].atk)
			self.players[playerid].sp -= attackCost
		elif ((messagelist[0] == "heal") and (self.players[playerid].sp >= healCost)):
			self.players[playerid].hp = self.players[playerid].maxHP
			self.players[playerid].sp -= healCost

		if checkWin(playerid):
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
	
	def handleShop(self, playerid, command, items):
		room = self.savedData['rooms'][self.players[playerid].location]
		if room["name"] in self.savedData['shops']:
			shopdata = self.savedData['shops'][room["name"]]
			nonexistentItems = []
			if command == "buy":
				for item in items:
					if item not in shopdata:
						self.writeMessage("Item {} is not in this shop".format(item))
					elif self.savedData['items'][item]['cost'] > self.players[playerid].money:
						self.writeMessage("You can't afford {}!!".format(item))
					else:
						self.players[playerid].money -= self.savedData['items'][item]['cost']
						if not self.addItem(playerid, item):
							break
			else:
				for item in items:
					if not removeItem(playerid, item):
						nonexistentItems.append(item)
					else:
						self.players[playerid].money += self.savedData['items'][item]['cost']//2
				if nonexistentItems:
					self.writeMessage("Error: Items {} not found".format(", ".join(nonexistentItems)))
		else:
			self.writeMessage("{} is not a shop".format(room))

	def handleItems(self, playerid, command, items):
		room = self.savedData['rooms'][self.players[playerid].location]
		nonexistentItems = []
		if command == "get":
			for item in items:
				if item in room["items"]:
					if not self.addItem(playerid, item):
						break;
					room["items"].remove(item)
				else:
					nonexistentItems.append(item)
		else:
			for item in items:
				if not self.removeItem(playerid, item):
					nonexistentItems.append(item)
				elif command == "drop":
					room["items"].append(item)
		if nonexistentItems:
			self.writeMessage("Error: Items {} not found".format(", ".join(nonexistentItems)))
		
	def useItems(self, playerid, message):
		items = message.split(", ")
		nonexistentItems = []
		for item in items:
			if item in self.players[playerid].items:
				itemdata = self.savedData["items"][item]
				if itemdata['type'] == "any":
					self.players[playerid].hp = min(self.players[playerid].maxHP, self.players[playerid].hp + itemdata['hp'])
					self.players[playerid].sp += itemdata['sp']
					if self.players[playerid].state == "battle":
						self.damageNPC(playerid, itemdata['atk'])
						self.checkWin(playerid)
				elif itemdata['type'] == "special":
					if self.players[playerid].state == 'battle':
						self.damageNPC(playerid, itemdata['atk'])
						self.checkWin(playerid)
					else:
						self.players[playerid].powerups.insert(item)
				elif (itemdata['type'] == "battle") and (self.players[playerid].state == "battle"):
					self.damageNPC(playerid, itemdata['atk'])
					self.checkWin(playerid)
				elif itemdata['type'] == "powerup":
					if item in ["bag", "suitcase"]:
						self.players[playerid].itemCapacity = itemdata['data']
					self.players[playerid].powerups.insert(item)
				else:
					self.writeMessage("Error: invalid item {}".format(item))
			else:
				nonexistentItems.append(item) 
		if nonexistentItems:
			self.writeMessage("Error: Items {} not found".format(", ".join(nonexistentItems)))
		
	def parseMessage(self,playerid,message):
		messagelist = message.split()
		if (DEBUG == 1):
			if (messagelist[0] == "modmove"):
				self.players[playerid].location = message[8:]
				return
			elif (messagelist[0] == "modmoney"):
				self.players[playerid].money += int(messagelist[1])
				return
		if (messagelist[0] == "use"):
			self.useItems(playerid, " ".join(messagelist[1:]))
		elif (self.players[playerid].state == "map"):
			if (messagelist[0] == "ride"):
				messagelist.pop(0)
				self.fastTravel(playerid,message[5:])
			elif (messagelist[0][:4] == 'inv'):
				self.printInventory(playerid)
			elif (messagelist[0] == "panic"):
				self.killPlayer(playerid)
			elif messagelist[0] in ["buy", "sell"]:
				command = messagelist[0]
				items = " ".join(messagelist[1:]).split(", ")
				self.handleShop(playerid, command, items)
			elif messagelist[0] in ["get", "drop", "destroy"]:
				command = messagelist[0]
				items = " ".join(messagelist[1:]).split(", ")
				self.handleItems(playerid, command, items)
			elif self.movePlayer(playerid,message):
				self.handleRoom(playerid)
		elif (self.players[playerid].state == "battle"):
			if (messagelist[0][:4] == "inv"):
				self.printState(playerid)
				self.printInventory(playerid)
			else:
				self.handleBattle(playerid, message)
