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
