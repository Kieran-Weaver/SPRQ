import json
import collections
import queue
import threading
import time
import random
import inspect
DEBUG = 1
#PlayerState is dynamic data, the saved json is static data
class PlayerState:
	hp = 20 # Goes down over time in battle
	sp = 10 # For using "attack", "block", and "heal"
	defMul = 1.0
	maxSP = 10
	maxHP = 20
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
		for pkey in self.savedData['players'][playerid]:
			setattr(self.players[playerid], pkey, self.savedData['players'][playerid][pkey])
		self.players[playerid].powerups = set(self.savedData['players'][playerid]['powerups'])
		if self.players[playerid].state == 'battle':
			self.players[playerid].battle['time'] = time.monotonic()
		
	def savePlayer(self,playerid):		
		self.savedData['players'][playerid] = {}
		playerstate = self.savedData['players'][playerid]
		playerdata = inspect.getmembers(self.players[playerid], lambda a:not(inspect.isroutine(a)))
		for data in playerdata:
			if not(data[0].startswith('_')):
				if type(data[1]) == set:
					playerstate[data[0]] = list(data[1])
				else:
					playerstate[data[0]] = data[1]
		
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
		if (room["npcs"]) and (random.randrange(0, 256) <= self.savedData['regions'][room["region"]]['npcrate']):
			self.setState(playerid, "battle")
			self.writeMessage(self.players[playerid].battle["text"]["entry"])
		if (room["spawner"]) and (room["spawner"] not in room["items"]):
			room["items"].append(room["spawner"])

	def damageNPC(self, playerid, atk):
		if self.players[playerid].state == "battle":
			if atk >= 0:
				self.players[playerid].battle["hp"] -= max(atk - self.players[playerid].battle["def"], 0)
			else:
				self.players[playerid].battle["hp"] += atk
		else:
			self.writeMessage("There is nothing to attack")

	def checkWin(self, playerid, usedItem):
		if (self.players[playerid].state == "battle") and (self.players[playerid].battle["hp"] <= 0):
			if usedItem:
				self.outqueue.put(self.players[playerid].battle["text"]["iwin"].format(usedItem))
			else:
				self.outqueue.put(self.players[playerid].battle["text"]["win"])
			self.players[playerid].money += self.players[playerid].battle["money"]
			for item in self.players[playerid].battle["drops"]:
				if (random.randrange(0, 256) <= self.players[playerid].battle["drops"][item]):
					self.addItem(playerid, item)
			self.setState(playerid, "map")
			return True
		else:
			return False
		
	def checkLose(self, playerid, usedItem):
		if (self.players[playerid].hp <= 0):
			if (self.players[playerid].battle["turn"] == 0):
				self.writeMessage(self.players[playerid].battle["text"]["plose"])
			elif usedItem:
				self.writeMessage(self.players[playerid].battle["text"]["ilose"].format(usedItem))
			else:
				self.writeMessage(self.players[playerid].battle["text"]["lose"])
			self.killPlayer(playerid)
			return True
		else:
			return False

	def doMove(self, playerid, message):
		if message in self.savedData["costs"]:
			cost = self.savedData["costs"][message]
			if (self.players[playerid].sp >= cost):
				self.players[playerid].sp -= cost
				return True
			else:
				self.writeMessage("You don't have enough sp to {}".format(message))
		return False
		
	def handleBattle(self,playerid, message, usedItem):
		messagelist = message.split()
		defMul = self.players[playerid].defMul
		if self.doMove(playerid, messagelist[0]):
			if messagelist[0] == "attack":
				self.damageNPC(playerid, self.players[playerid].atk)
			elif messagelist[0] == "heal":
				self.players[playerid].hp = self.players[playerid].maxHP
			elif messagelist[0] == "block":
				defMul = self.players[playerid].defMul/2

		if self.checkWin(playerid, usedItem):
			return

		self.players[playerid].hp -= round(defMul*self.players[playerid].battle["atk"]*(time.monotonic() - self.players[playerid].battle["time"]))
		if not self.checkLose(playerid, usedItem):
			self.writeMessage(self.players[playerid].battle["text"]["turn"])
			self.players[playerid].battle['time'] = time.monotonic()
			self.players[playerid].battle['turn'] += 1
		
	def setState(self, playerid, state):
		if (state == "map"):
			self.players[playerid].battle = {}
			self.players[playerid].state = "map"
		elif (state == "battle"):
			room = self.savedData['rooms'][self.players[playerid].location]
			self.players[playerid].battle = self.savedData["npcs"][room["npcs"][0]].copy()
			self.players[playerid].battle['time'] = time.monotonic()
			self.players[playerid].battle['turn'] = 0
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
		self.players[playerid].money = 0
		self.players[playerid].location = self.savedData['regions'][room['region']]['room']
		self.setState(playerid, "map")
		self.writeMessage(self.savedData['regions'][room['region']]['message'])
		self.players[playerid].hp = self.players[playerid].maxHP
		self.players[playerid].sp = self.players[playerid].maxSP

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
					if not self.removeItem(playerid, item):
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
		
	def attackItem(self, playerid, item):
		damage = self.savedData["items"][item]["atk"]
		weakness = "soup"
		if "weakness" in self.players[playerid].battle:
			weakness = self.players[playerid].battle["weakness"]
		if weakness == item:
			damage = damage * 2
		self.damageNPC(playerid, damage)

	def useItems(self, playerid, message):
		items = message.split(", ")
		nonexistentItems = []
		lastItem = ""
		for item in items:
			if item in self.players[playerid].items:
				itemdata = self.savedData["items"][item]
				if itemdata['type'] == "any":
					self.players[playerid].hp = min(self.players[playerid].maxHP, self.players[playerid].hp + itemdata['hp'])
					self.players[playerid].sp = min(self.players[playerid].maxSP, self.players[playerid].sp + itemdata['sp'])
					if self.players[playerid].state == "battle":
						self.attackItem(playerid, item)
						lastItem = item
				elif itemdata['type'] == "special":
					if self.players[playerid].state == 'battle':
						self.attackItem(playerid, item)
						lastItem = item
					else:
						self.players[playerid].powerups.add(item)
				elif (itemdata['type'] == "battle") and (self.players[playerid].state == "battle"):
					self.attackItem(playerid, itemdata['atk'])
					lastItem = item
				elif itemdata['type'] == "powerup":
					if item in ["bag", "suitcase"]:
						self.players[playerid].itemCapacity = itemdata['data']
					self.players[playerid].powerups.add(item)
				else:
					self.writeMessage("Error: invalid item {}".format(item))
				self.removeItem(playerid, item)
			else:
				nonexistentItems.append(item)
		if nonexistentItems:
			self.writeMessage("Error: Items {} not found".format(", ".join(nonexistentItems)))
		if self.players[playerid].state == "battle":
			self.handleBattle(playerid, message, item)
		
	def parseMessage(self,playerid,message):
		messagelist = message.split()
		if (DEBUG == 1):
			if (messagelist[0] == "modmove"):
				self.players[playerid].location = message[8:]
				return
			elif (messagelist[0] == "modmoney"):
				self.players[playerid].money += int(messagelist[1])
				return
			elif (messagelist[0] == "modgive"):
				self.addItem(playerid, messagelist[1])
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
			elif messagelist[0] == "profile":
				player = self.players[playerid]
				self.writeMessage("HP: {}".format(player.hp))
				self.writeMessage("SP: {}".format(player.sp))
				self.writeMessage("XP: {}".format(player.xp))
				self.writeMessage("Money: {}".format(player.money))
			elif self.movePlayer(playerid,message):
				self.handleRoom(playerid)
		elif (self.players[playerid].state == "battle"):
			if (messagelist[0][:4] == "inv"):
				self.printState(playerid)
				self.printInventory(playerid)
			elif messagelist[0] in ["attack", "heal", "block"]:
				self.handleBattle(playerid, message, False)
			elif random.randrange(0, 256) > 100:
				self.writeMessage(self.players[playerid].battle["text"]["norun"])
				self.killPlayer(playerid)
			elif self.movePlayer(playerid, message): 
				self.writeMessage(self.players[playerid].battle["text"]["run"])
				self.setState(playerid, "map")
			else:
				self.handleBattle(playerid, message, False)
