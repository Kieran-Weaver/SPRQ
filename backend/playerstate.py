from queue import SimpleQueue
from collections import Counter
import random
from .rqflags import *
levelupTable = {
	"HP": ("maxHP", 10),
	"SP": ("maxSP", 5),
	"ATTACK": ("atk", 1),
	"DEFENSE": ("defStat", 1)
}
class PlayerState:
	def __init__(self):
#    Battle Stats
		self.hp = 20           # Current HP
		self.sp = 10           # Current SP for using "attack", "block", and "heal"
		self.atk = 1           # Current attack stat
		self.defMul = 1.0      # Defense multiplier
		self.defStat = 0       # Internal defense stat
#    Max Stats
		self.maxHP = 20        # Max HP
		self.maxSP = 10        # Max SP
		self.itemCapacity = 10 # Max # of items you can hold
#    Game progress / Save data
		self.state = "map"     # Determines actions you can take
		self.location = "UTP Lounge"
		self.items = Counter() # Dict of items in the form { "item" : count }
		self.lockerItems = {}  # Dict of items in storage, accessible at lockers and all shops
		self.powerups = set()  # Set of powerups
		self.battle = {}       # Current Battle data
		self.xp = 0            # Current xp, 100 needed until next level-up
		self.level = 1         # Current level
		self.levelpoints = 0   # Stored level points, which you can put toward HP, SP, attack, or defense
		self.money = 0         # Current money
		self._outqueue = SimpleQueue() # Player messages
		self.mode = RQMode.M_15# Mode, determines flags
		self._items = None
		self.frozen = False    # Frozen players don't receive output

	def writeMessage(self, message):
		if not self.frozen:
			self._outqueue.put(message)

	def numItems(self):
		return sum(self.items.values())

	def addItem(self, item):
		if self.mode == RQMode.M_RAND:
			item = random.choice(self._items)
		if self.numItems() < self.itemCapacity:
			self.items[item] = self.items.get(item, 0) + 1
			self.writeMessage(f"You got a {item}!")
			return True
		else:
			self.writeMessage("You cannot pick up any more items!")
			return False

	def removeItem(self, item):
		if item in self.items:
			self.items[item] -= 1
			self.items = +(self.items)
			return True
		else:
			return False

	def addXP(self, xp, level):
		if (self.level > level):
			self.xp += math.ceil(xp / (self.level - level))
		else:
			self.xp += xp
		if (self.xp >= 100):
			self.level += 1
			self.levelpoints += 1
			self.xp -= 100
			self.writeMessage("You received one level point!")
			self.writeMessage("Type levelup STAT to increase one of your stats")
			self.writeMessage("Stats you can level up:")
			self.writeMessage("HP, SP, Attack, and Defense")
			return True
		else:
			return False

	def levelUp(self, stat):
		if not self.levelpoints:
			self.writeMessage("You have 0 level points and cannot level up a stat!")
			return False
		elif stat.upper() in levelupTable:
			self.writeMessage(f"You leveled up: {stat}")
			statboost = levelupTable[stat.upper()]
			setattr(self, statboost[0], getattr(self, statboost[0]) + statboost[1])
			self.hp = self.players[playerid].maxHP
			self.sp = self.players[playerid].maxSP
			self.levelpoints -= 1
			return True
		else:
			self.writeMessage(f"{stat} is not a stat you can level up!")
			return False

	def printStats(self):
		self.writeMessage(f"HP: {self.hp}/{self.maxHP}")
		self.writeMessage(f"SP: {self.sp}/{self.maxSP}")
		self.writeMessage(f"Attack: {self.atk}")
		self.writeMessage(f"Defense: {self.defStat}")
		self.writeMessage(f"XP: {self.xp}/100")
	
	def getMessages(self):
		messages = []
		while not self._outqueue.empty():
			messages.append(self._outqueue.get())
		return messages

	def printInventory(self):
		self.writeMessage(f"Money: {self.money}")
		self.writeMessage("Items: ")
		for key in self.items:
			keystr = f"{key}"
			if self.items[key] > 1:
				keystr = f"{key} x {self.items[key]}"
			self.writeMessage(keystr)
	
	def reset(self):
		items = self.items.elements()
		self.items = Counter()
		if self.hasFlag(RQFlags.F_DEATH_MONEY):
			self.money = 0
		self.hp = self.maxHP
		self.sp = self.maxSP
		return items
	
	def damageNPC(self, atk):
		if self.state == "battle":
			if atk >= 0: # Not piercing
				self.battle["hp"] -= max(atk - self.battle["def"], 0)
			else: # Piercing
				self.battle["hp"] += atk
		else:
			self.writeMessage("There is nothing to attack")

	def hasFlag(self, flag):
		return flag in getFlags(self.mode)
