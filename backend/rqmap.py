import random
import time
from .rqflags import *
class RQMap:
	def __init__(self, saveddata, players):
		self.savedData = saveddata
		self.players = players
		self.directions = ["north", "south", "east", "west", "n", "s", "e", "w"]
		self.battles = {}

	def getRoom(self, playerid):
		if self.players[playerid].location == "In Locker":
			return {
				"exits":["none","none","none","none"],
				"info":"You are inside your locker",
				"items":self.players[playerid].lockerItems,
				"name":"In Locker",
				"npcs":[],
				"region":"UBC",
				"spawner":None
			}
		else:
			return self.savedData["rooms"][self.players[playerid].location]

	def movePlayer(self, playerid, exitname):
		if self.players[playerid].mode == RQMode.M_RAND:
			self.players[playerid].location = random.choice([*self.savedData["rooms"].keys()])
			return True
		room = self.getRoom(playerid)
		reenter = self.players[playerid].hasFlag(RQFlags.F_REENTER_GLITCH)
		if exitname in self.directions:
			exitindex = self.directions.index(exitname) % 4
			if room["exits"][exitindex] == "none":
				self.players[playerid].writeMessage("That is not an exit")
				if not reenter:
					return False
			else:
				self.players[playerid].location = room["exits"][exitindex]
		elif exitname in room["exits"]:
			self.players[playerid].location = exitname
		else:
			self.players[playerid].writeMessage("That is not an exit")
			if not reenter:
				return False
		return True

	def fastTravel(self, playerid, message):
		if message in self.savedData["fast-travel"]:
			stops = self.savedData["fast-travel"][message]
			if self.players[playerid].location in stops:
				cost = 100
				if message[5:16].lower() == "canada line":
					cost = 200
				if self.players[playerid].money < cost:
					self.players[playerid].writeMessage( "Not enough money to ride")
				else:
					self.players[playerid].money -= cost
					self.players[playerid].location = message
			else:
				self.players[playerid].writeMessage( "You cannot ride that here!")
		else:
			self.players[playerid].writeMessage( f"{message} is not a route")

	def handleRoom(self, playerid):
		room = self.getRoom(playerid)
		if room["npcs"]:
			npcrate = self.savedData["regions"][room["region"]]["npcrate"]
			if any(x in self.savedData["bosses"] for x in room["npcs"]):
				npcrate = 256
			if random.randrange(256) <= npcrate:
				if self.players[playerid].mode == RQMode.M_COOP:
					if room["name"] in self.battles:
						if playerid not in self.battles[room["name"]]:
							self.battles[room["name"]].append(playerid)
					else:
						self.battles[room["name"]] = [playerid]
				if not self.setState(playerid, "battle"):
					return
				self.players[playerid].writeMessage(self.players[playerid].battle["text"]["entry"])

		if room["spawner"] and room["spawner"] not in room["items"]:
			room["items"][room["spawner"]] = room["items"].get(room["spawner"], 0) + 1

	def setState(self, playerid, state):
		if state == "map":
			self.players[playerid].battle = {}
			self.players[playerid].state = "map"
			if self.players[playerid].location in self.battles:
				while playerid in self.battles[self.players[playerid].location]:
					self.battles[self.players[playerid].location].remove(playerid)
		elif state == "battle":
			room = self.getRoom(playerid)
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
			if self.players[playerid].battle["hp"] == 0:
				self.setState(playerid, "map")
				return False
			if self.players[playerid].mode == RQMode.M_COOP and room['name'] in self.battles:
				if self.battles[room["name"]].index(playerid) != 0:
					newid = self.battles[room["name"]][0]
					self.players[playerid].battle = self.players[newid].battle
		elif DEBUG == 1:
			self.players[playerid].writeMessage( f"Invalid state: {state}")
		return True
	
	def getNextPlayer(self, playerid):
		if self.players[playerid].mode == RQMode.M_COOP and self.players[playerid].state == "battle":
			room = self.getRoom(playerid)
			pindex = self.battles[room["name"]].index(playerid)
			nextPlayer = self.battles[room["name"]][(pindex + 1) % len(self.battles[room["name"]])]
			if nextPlayer != playerid:
				return nextPlayer
			else:
				return None
		else:
			return None
