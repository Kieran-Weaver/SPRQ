import json
import inspect
from .playerstate import PlayerState
class JSONHandler:
	def __init__(self, filename):
		self.loadState(filename)

	def __getitem__(self, key):
		return self.savedData[key]

	def __setitem__(self, key, value):
		self.savedData[key] = value

	def __delitem__(self, key):
		del self.savedData[key]

	def loadState(self, filename=None):
		if filename:
			with open(filename, "r") as f:
				self.savedData = json.load(f)
			self.filename = filename
		elif self.filename:
			with open(self.filename, "r") as f:
				self.savedData = json.load(f)
#       else: fail silently

	def saveState(self, filename = None):
		if not filename:
			filename = self.filename
		with open(filename, "w") as f:
			json.dump(self.savedData, f, indent=2)

	def loadPlayer(self, playerid):
		player = PlayerState()
		if not (playerid in self.savedData["players"]):
			self.savePlayer(playerid, player)
		for pkey in self.savedData["players"][playerid]:
			setattr(player, pkey, self.savedData["players"][playerid][pkey])
		player.powerups = set(self.savedData["players"][playerid]["powerups"])
		if player.state == "battle":
			player.battle["time"] = time.monotonic()
		return player
	
	def savePlayer(self, playerid, player):
		self.savedData["players"][playerid] = {}
		playerstate = self.savedData["players"][playerid]
		playerdata = inspect.getmembers(player, lambda a: not(inspect.isroutine(a)))
		for data in playerdata:
			if not data[0].startswith("_"):
				if type(data[1]) in [list, set]:
					playerstate[data[0]] = list(data[1])
				elif type(data[1]) == dict:
					playerstate[data[0]] = dict(data[1])
				else:
					playerstate[data[0]] = data[1]
