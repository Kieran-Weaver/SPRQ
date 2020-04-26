import json
import queue
import time
import random
import inspect
import math
import itertools
DEBUG = 1
# PlayerState is dynamic data, the saved json is static data
levelupTable = {
	"HP": ("maxHP", 10),
	"SP": ("maxSP", 5),
	"ATTACK": ("atk", 1),
	"DEFENSE": ("defStat", 1)
}


class PlayerState:
	hp = 20  # Goes down over time in battle
	sp = 10  # For using "attack", "block", and "heal"
	defMul = 1.0
	defStat = 0
	maxSP = 10
	maxHP = 20
	itemCapacity = 10
	atk = 1
	xp = 0
	level = 1
	levelpoints = 0
	money = 0
	location = "UTP Lounge"
	items = {}
	state = "map"
	battle = {}
	powerups = set()
	status = {}


class RQState:
	savedData = {}
	players = {}
	outqueue = queue.SimpleQueue()

	def __init__(self, filename):
		with open(filename, "r") as f:
			self.savedData = json.load(f)
		for player in self.savedData["players"]:
			self.loadPlayer(player)

	def savestate(self, filename):
		for player in self.players:
			self.savePlayer(player)
		with open(filename, "w") as f:
			json.dump(self.savedData, f, indent=2)

	def writeMessage(self, message):
		self.outqueue.put(message)

	def numItems(self, playerid):
		return sum(self.players[playerid].items.values())

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

	def addXP(self, playerid, xp, level):
		playerdata = self.players[playerid]
		if (playerdata.level > level):
			playerdata.xp += math.ceil(xp / (playerdata.level - level))
		else:
			playerdata.xp += xp
		if (playerdata.xp >= 100):
			playerdata.level += 1
			playerdata.levelpoints += 1
			playerdata.xp -= 100
			self.writeMessage("You received one level point!")
			self.writeMessage("Type levelup STAT to increase one of your stats")
			self.writeMessage("Stats you can level up:")
			self.writeMessage("HP, SP, Attack, and Defense")

	def levelUp(self, playerid, stat):
		if (self.players[playerid].levelpoints == 0):
			self.writeMessage("You have 0 level points and cannot level up a stat!")
		elif stat.upper() in levelupTable:
			self.writeMessage(f"You leveled up: {stat}")
			statboost = levelupTable[stat.upper()]
			setattr(self.players[playerid], statboost[0], getattr(self.players[playerid], statboost[0]) + statboost[1])
			self.players[playerid].hp = self.players[playerid].maxHP
			self.players[playerid].sp = self.players[playerid].maxSP
			self.players[playerid].levelpoints -= 1
			self.printInventory(playerid)
		else:
			self.writeMessage(f"{stat} is not a stat you can level up!")

	def loadPlayer(self, playerid):
		self.players[playerid] = PlayerState()
		if not (playerid in self.savedData["players"]):
			self.savePlayer(playerid)
		for pkey in self.savedData["players"][playerid]:
			setattr(self.players[playerid], pkey, self.savedData["players"][playerid][pkey])
		self.players[playerid].powerups = set(self.savedData["players"][playerid]["powerups"])
		if self.players[playerid].state == "battle":
			self.players[playerid].battle["time"] = time.monotonic()

	def savePlayer(self, playerid):
		self.savedData["players"][playerid] = {}
		playerstate = self.savedData["players"][playerid]
		playerdata = inspect.getmembers(self.players[playerid], lambda a: not(inspect.isroutine(a)))
		for data in playerdata:
			if not data[0].startswith("_"):
				if type(data[1]) in [list, set]:
					playerstate[data[0]] = list(data[1])
				elif type(data[1]) == dict:
					playerstate[data[0]] = dict(data[1])
				else:
					playerstate[data[0]] = data[1]

	def movePlayer(self, playerid, exitname):
		directions = ["north", "south", "east", "west", "n", "s", "e", "w"]
		if exitname in directions:
			exitindex = directions.index(exitname) % 4
			if self.savedData["rooms"][self.players[playerid].location]["exits"][exitindex] == "none":
				self.writeMessage("That is not an exit")
				return False
			else:
				self.players[playerid].location = self.savedData["rooms"][self.players[playerid].location]["exits"][exitindex]
		elif exitname in self.savedData["rooms"][self.players[playerid].location]["exits"]:
			self.players[playerid].location = exitname
		else:
			self.writeMessage("That is not an exit")
			return False
		return True

	def handleRoom(self, playerid):
		room = self.savedData["rooms"][self.players[playerid].location]
		if room["npcs"]:
			npcrate = self.savedData["regions"][room["region"]]["npcrate"]
			if any(x in self.savedData["bosses"] for x in room["npcs"]):
				npcrate = 256
			if random.randrange(256) <= npcrate:
				self.setState(playerid, "battle")
				self.writeMessage(self.players[playerid].battle["text"]["entry"])
		if room["spawner"] and room["spawner"] not in room["items"]:
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
		if self.players[playerid].state == "battle" and self.players[playerid].battle["hp"] <= 0:
			if usedItem not in ["attack", "heal", "block"]:
				self.outqueue.put(self.players[playerid].battle["text"]["iwin"].format(usedItem))
			else:
				self.outqueue.put(self.players[playerid].battle["text"]["win"].format(usedItem))
			self.players[playerid].money += self.players[playerid].battle["money"]
			for item in self.players[playerid].battle["drops"]:
				if random.randrange(256) <= self.players[playerid].battle["drops"][item]:
					self.addItem(playerid, item)
			self.addXP(playerid, self.players[playerid].battle["xp"], self.players[playerid].battle["level"])
			self.setState(playerid, "map")
			return True
		else:
			return False

	def checkLose(self, playerid, usedItem):
		if self.players[playerid].hp <= 0:
			if self.players[playerid].battle["turn"] == 0:
				self.writeMessage(self.players[playerid].battle["text"]["plose"])
			elif usedItem:
				self.writeMessage(self.players[playerid].battle["text"]["ilose"].format(usedItem))
			else:
				self.writeMessage(self.players[playerid].battle["text"]["lose"].format(usedItem))
			self.killPlayer(playerid)
			return True
		else:
			return False

	def doMove(self, playerid, message):
		if message in self.savedData["costs"]:
			cost = self.savedData["costs"][message]
			if self.players[playerid].sp >= cost:
				self.players[playerid].sp -= cost
				return True
			else:
				self.writeMessage(f"You don't have enough sp to {message}")
		return False

	def handleBattle(self, playerid, message, usedItem):
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

		damage = self.players[playerid].battle["atk"]
		message = self.players[playerid].battle["text"]["turn"]
		if self.players[playerid].battle["type"] == "bosses":
			attacks = self.players[playerid].battle["attacks"]
			rChoices = []
			if "charge" in self.players[playerid].battle:  # Boss is charged
				rChoices = ["charge", "catk"]
			else:  # Boss is not charged
				rChoices = [x for x in attacks.keys() if x != "catk" and self.players[playerid].battle["hp"] <= attacks[x]["maxhp"]]
			rWeights = [*itertools.accumulate([attacks[x]["probability"] for x in rChoices]), 256]
			rChoices.append(None)
			chosen = random.choices(rChoices, cum_weights=rWeights)[0]
			if chosen == "charge":
				self.players[playerid].battle["charge"] = self.players[playerid].battle.get("charge") + attacks[chosen]["atk"]
				damage = 0
				message = attacks[chosen]["text"]
			elif chosen == "catk":
				damage = self.players[playerid].battle["charge"] + attacks[chosen]["atk"]
				message = attacks[chosen]["text"]
			elif chosen:
				damage = attacks[chosen]["atk"]
				message = attacks[chosen]["text"]

		self.players[playerid].hp -= round(defMul * damage * (time.monotonic() - self.players[playerid].battle["time"]))
		if not self.checkLose(playerid, usedItem):
			self.writeMessage(message)
			self.players[playerid].battle["time"] = time.monotonic()
			self.players[playerid].battle["turn"] += 1

	def setState(self, playerid, state):
		if state == "map":
			self.players[playerid].battle = {}
			self.players[playerid].state = "map"
		elif state == "battle":
			room = self.savedData["rooms"][self.players[playerid].location]
			npcname = random.choice(room["npcs"])
			battletype = ""
			if npcname in self.savedData["npcs"]:
				battletype = "npcs"
			elif npcname in self.savedData["bosses"]:
				battletype = "bosses"
			self.players[playerid].battle = self.savedData[battletype][npcname].copy()
			self.players[playerid].battle["time"] = time.monotonic()
			self.players[playerid].battle["turn"] = 0
			self.players[playerid].battle["type"] = battletype
			self.players[playerid].state = "battle"
		else:
			if DEBUG == 1:
				self.writeMessage(f"Invalid state: {state}")

	def killPlayer(self, playerid):
		room = self.savedData["rooms"][self.players[playerid].location]
		for key in self.players[playerid].items:
			for i in range(self.players[playerid].items[key]):
				self.savedData["rooms"][room["name"]]["items"].append(key)
		self.players[playerid].items = {}
		self.players[playerid].money = 0
		self.players[playerid].location = self.savedData["regions"][room["region"]]["room"]
		self.setState(playerid, "map")
		self.writeMessage(self.savedData["regions"][room["region"]]["message"])
		self.players[playerid].hp = self.players[playerid].maxHP
		self.players[playerid].sp = self.players[playerid].maxSP

	def printState(self, playerid):
		player = self.players[playerid]
		if player.state == "map":
			room = self.savedData["rooms"][self.players[playerid].location]
			rmessage = [room["name"], room["info"], "Items:"] + room["items"]
			if "flashlight" in self.players[playerid].powerups:
				rmessage.append("Exits: ")
				rmessage += [x for x in room["exits"] if x != "none"]
#			rmessage = rmessage + ["People Here:"] + rooms["players"]
			rmessage.append("Region: " + room["region"])
			self.writeMessage("\n".join(rmessage))
		elif player.state == "battle":
			self.writeMessage(f"HP: {player.hp}")
			self.writeMessage(f"SP: {player.sp}")
			self.writeMessage(f"NPC Name: {self.players[playerid].battle['name']}")
			self.writeMessage(f"NPC HP: {self.players[playerid].battle['hp']}")

	def printInventory(self, playerid):
		self.writeMessage(f"Money: {self.players[playerid].money}")
		self.writeMessage("Items: ")
		for key in self.players[playerid].items:
			keystr = str(key)
			if self.players[playerid].items[key] > 1:
				keystr += f" x {self.players[playerid].items[key]}\n"
			self.writeMessage(keystr)

	def fastTravel(self, playerid, message):
		if message in self.savedData["fast-travel"]:
			stops = self.savedData["fast-travel"][message]
			if self.players[playerid].location in stops:
				cost = 100
				if message[5:16].lower() == "canada line":
					cost = 200
				if self.players[playerid].money < cost:
					self.writeMessage("Not enough money to ride")
				else:
					self.players[playerid].money -= cost
					self.players[playerid].location = message
			else:
				self.writeMessage("You cannot ride that here!")
		else:
			self.writeMessage(f"{message} is not a route")

	def handleShop(self, playerid, command, items):
		room = self.savedData["rooms"][self.players[playerid].location]
		if room["name"] in self.savedData["shops"]:
			shopdata = self.savedData["shops"][room["name"]]
			nonexistentItems = []
			if command == "buy":
				for item in items:
					if item not in shopdata:
						self.writeMessage(f"Item {item} is not in this shop")
					elif self.savedData["items"][item]["cost"] > self.players[playerid].money:
						self.writeMessage(f"You can't afford {item}!!")
					else:
						self.players[playerid].money -= self.savedData["items"][item]["cost"]
						if not self.addItem(playerid, item):
							break
			else:
				for item in items:
					if not self.removeItem(playerid, item):
						nonexistentItems.append(item)
					else:
						self.players[playerid].money += self.savedData["items"][item]["cost"]//2
				if nonexistentItems:
					self.writeMessage(f"Error: Items {', '.join(nonexistentItems)} not found")
		else:
			self.writeMessage(f"{room} is not a shop")

	def handleItems(self, playerid, command, items):
		room = self.savedData["rooms"][self.players[playerid].location]
		nonexistentItems = []
		if command == "get":
			for item in items:
				if item in room["items"]:
					if not self.addItem(playerid, item):
						break
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
			self.writeMessage(f"Error: Items {', '.join(nonexistentItems)} not found")

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
				if itemdata["type"] == "any":
					self.players[playerid].hp = min(self.players[playerid].maxHP, self.players[playerid].hp + itemdata["hp"])
					self.players[playerid].sp = min(self.players[playerid].maxSP, self.players[playerid].sp + itemdata["sp"])
					if self.players[playerid].state == "battle":
						self.attackItem(playerid, item)
						lastItem = item
				elif itemdata["type"] == "special":
					if self.players[playerid].state == "battle":
						self.attackItem(playerid, item)
						lastItem = item
					else:
						self.players[playerid].powerups.add(item)
				elif itemdata["type"] == "battle" and self.players[playerid].state == "battle":
					self.attackItem(playerid, itemdata["atk"])
					lastItem = item
				elif itemdata["type"] == "powerup":
					if item in ["bag", "suitcase"]:
						self.players[playerid].itemCapacity = itemdata["data"]
					self.players[playerid].powerups.add(item)
				else:
					self.writeMessage(f"Error: invalid item {item}")
				self.removeItem(playerid, item)
			else:
				nonexistentItems.append(item)
		if nonexistentItems:
			self.writeMessage(f"Error: Items {', '.join(nonexistentItems)} not found")
		if self.players[playerid].state == "battle":
			self.handleBattle(playerid, message, item)

	def openDispenser(self, playerid, message):
		if message not in self.savedData["dispensers"]["rooms"].keys():
			self.writeMessage(f"You can't open {message}!")
		elif self.players[playerid].location not in self.savedData["dispensers"]["rooms"][message]:
			self.writeMessage(f"You can't {message} here!")
		else:
			dispenserDict = self.savedData["dispensers"][message]
			item = random.choices([*dispenserDict.keys()], weights=dispenserDict.values())[0]
			self.addItem(playerid, item)

	def parseMessage(self, playerid, message):
		messagelist = message.split()
		if DEBUG == 1:
			if messagelist[0] == "modmove":
				self.players[playerid].location = message[8:]
				return
			elif messagelist[0] == "modmoney":
				self.players[playerid].money += int(messagelist[1])
				return
			elif messagelist[0] == "modgive":
				self.addItem(playerid, messagelist[1])
				return
			elif messagelist[0] == "modxp":
				self.addXP(playerid, int(messagelist[1]), 1)
				return
			elif messagelist[0] == "modlevel":
				self.players[playerid].level = int(messagelist[1])
				return

		if messagelist[0] == "use":
			self.useItems(playerid, " ".join(messagelist[1:]))
		elif self.players[playerid].state == "map":
			if messagelist[0] == "ride":
				messagelist.pop(0)
				self.fastTravel(playerid, message[5:])
			elif messagelist[0][:4] == "inv":
				self.printInventory(playerid)
			elif messagelist[0] == "panic":
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
				self.writeMessage(f"HP: {player.hp}")
				self.writeMessage(f"SP: {player.sp}")
				self.writeMessage(f"XP: {player.xp}")
				self.writeMessage(f"Money: {player.money}")
			elif messagelist[0] == "levelup":
				self.levelUp(playerid, messagelist[1])
			elif messagelist[0] == "open":
				self.openDispenser(playerid, messagelist[1])
			elif self.movePlayer(playerid, message):
				self.handleRoom(playerid)
		elif self.players[playerid].state == "battle":
			if messagelist[0][:4] == "inv":
				self.printState(playerid)
				self.printInventory(playerid)
			elif messagelist[0] in ["attack", "heal", "block"]:
				self.handleBattle(playerid, message, messagelist[0])
			elif random.randrange(256) > 100:
				self.writeMessage(self.players[playerid].battle["text"]["norun"])
				self.killPlayer(playerid)
			elif self.movePlayer(playerid, message):
				self.writeMessage(self.players[playerid].battle["text"]["run"])
				self.setState(playerid, "map")
			else:
				self.handleBattle(playerid, message, False)
