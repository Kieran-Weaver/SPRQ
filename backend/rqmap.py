import random
import time
class RQMap:
	def __init__(self, saveddata):
		self.savedData = saveddata
		self.directions = ["north", "south", "east", "west", "n", "s", "e", "w"]

	def getRoom(self, playerdata):
		return self.savedData["rooms"][playerdata.location]

	def movePlayer(self, playerdata, exitname):
		room = self.getRoom(playerdata)
		if exitname in self.directions:
			exitindex = self.directions.index(exitname) % 4
			if room["exits"][exitindex] == "none":
				playerdata.writeMessage("That is not an exit")
				return False
			else:
				playerdata.location = room["exits"][exitindex]
		elif exitname in room["exits"]:
			playerdata.location = exitname
		else:
			playerdata.writeMessage("That is not an exit")
			return False
		return True

	def fastTravel(self, playerdata, message):
		if message in self.savedData["fast-travel"]:
			stops = self.savedData["fast-travel"][message]
			if playerdata.location in stops:
				cost = 100
				if message[5:16].lower() == "canada line":
					cost = 200
				if playerdata.money < cost:
					playerdata.writeMessage( "Not enough money to ride")
				else:
					playerdata.money -= cost
					playerdata.location = message
			else:
				playerdata.writeMessage( "You cannot ride that here!")
		else:
			playerdata.writeMessage( f"{message} is not a route")

	def handleRoom(self, playerdata):
		room = self.getRoom(playerdata)
		if room["npcs"]:
			npcrate = self.savedData["regions"][room["region"]]["npcrate"]
			if any(x in self.savedData["bosses"] for x in room["npcs"]):
				npcrate = 256
			if random.randrange(256) <= npcrate:
				self.setState(playerdata, "battle")
				playerdata.writeMessage(playerdata.battle["text"]["entry"])
		if room["spawner"] and room["spawner"] not in room["items"]:
			room["items"].append(room["spawner"])

	def setState(self, playerdata, state):
		if state == "map":
			playerdata.battle = {}
			playerdata.state = "map"
		elif state == "battle":
			room = self.getRoom(playerdata)
			npcname = random.choice(room["npcs"])
			battletype = ""
			if npcname in self.savedData["npcs"]:
				battletype = "npcs"
			elif npcname in self.savedData["bosses"]:
				battletype = "bosses"
			playerdata.battle = self.savedData[battletype][npcname].copy()
			playerdata.battle["time"] = time.monotonic()
			playerdata.battle["turn"] = 0
			playerdata.battle["type"] = battletype
			playerdata.state = "battle"
		elif DEBUG == 1:
			playerdata.writeMessage( f"Invalid state: {state}")
