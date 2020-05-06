import re
import os
import json
import ast
import string
import collections
import inspect
import rqdata.rooms

itemtable = {
	"🍰" : "cake",
	"🥘" : "soup",
	"💌" : "letter",
	"🛡️" : "shield",
	"🕯️" : "candle",
	"❄️" : "snowflake",
	"📝" : "script",
	"🍃" : "leaf",
	"🌱" : "seed",
	"🚩" : "flag",
	"🍩" : "donut",
	"📰" : "news",
	"🥖" : "baguette",
	"🍂" : "leaf",
	"✏️" : "pencil",
	"🌻" : "flower",
	"🌾" : "plant",
	"⚽" : "soccer_ball",
	"🏀" : "basketball",
	"🔑" : "key",
	"🍁" : "leaf",
	"📣" : "megaphone",
	"🔦" : "flashlight",
	"📇" : "bus pass",
	"🕳️" : "hole",
	"👜" : "bag",
	"🛄" : "suitcase",
	"♨️" : "repel",
	"🎟️" : "ticket",
	"🎱" : "ball",
	"🎳" : "bowling",
	"👟" : "shoe",
	"🔓" : "lock",
	"🛒" : "cart",
	"📡" : "satellite",
	"🥗" : "salad",
	"🌨️" : "snowcloud",
	"📀" : "disk",
	"🔋" : "battery",
	"🧀" : "cheese",
	"🔍" : "glass",
	"📔" : "notebook",
	"🖍️" : "crayon",
	"☘️" : "clover",
	"🐟" : "fish",
	"🐠" : "rare fish",
	"🎈" : "balloon",
	"🥛" : "milk",
	"❤️" : "heart"
}

def GenRoomJSON(room):
	roomjson = {}
	if room.dexits != None:
		new_exits = set(room.exits) - set(room.dexits)
		room.dexits += [*new_exits]
		room.exits = room.dexits	
	del room.dexits
	try:
		room.spawner = itemtable[room.spawner]
	except:
		room.spawner = None
	roomdata = inspect.getmembers(room, lambda a: not(inspect.isroutine(a)))
	for data in roomdata:
		if not data[0].startswith("_"):
			if type(data[1]) in [list, set]:
				roomjson[data[0]] = list(data[1])
			elif type(data[1]) == dict:
				roomjson[data[0]] = dict(data[1])
			else:
				roomjson[data[0]] = data[1]
	roomjson["items"] = {}
	return roomjson

def GenRespawnJSON(spawnpoints,rmessages):
	regions = spawnpoints.keys()
	rdata = {}
	for key in regions:
		rdata[key] = {'room':spawnpoints[key],'message':rmessages[key], 'npcrate' : 26}
	return rdata

def GenBusJSON(busdict):
	bdata = {}
	for k in busdict.keys():
		for v in busdict[k]:
			if not v in bdata.keys():
				bdata[v] = []
			bdata[v].append(k)
	return bdata

#drops out of 256
gamedata = {
	'rooms' : {
	},
	'regions' : {
	},
	'fast-travel' : {
	},
	'players' : {
	},
	'shops' : {
		"UBC Bookstore" : ["soup", "healthy soup", "souper soup", "flashlight", "bus_pass"],
		"YuBot Gift Shop Downtown Vancouver" : ["soup", "souper soup", "flashlight", "bus_pass"],
		"YuBot Gift Shop Granville Island" : ["soup", "souper soup", "flashlight", "bus_pass"],
		"YuBot Gift Shop False Creek South" : ["soup", "souper soup", "flashlight", "bus_pass"],
		"rqSHOP False Creek South" : ["satellite"],
		"RQ Storage Solutions False Creek South" : ["bag", "suitcase"],
		"YuBot Gift Shop Kerrisdale" : ["soup", "souper soup", "flashlight", "bus pass"],
		"rqSHOP Kerrisdale" : ["repel"],
		"YuBot Gift Shop Brighouse" : ["soup", "souper soup", "flashlight", "bus pass"],
		"rqSHOP Brighouse" : ["lock", "suitcase", "sattelite"],
		"rqSHOP Wesbrook Village" : ["soup", "souper soup", "battle soup", "health soup"],
		"YuBot Gift Shop Commercial-Broadway" : ["soup", "souper soup", "flashlight", "bus pass"],
		"YuBot Gift Shop Crystal Mall" : ["soup", "souper soup", "flashlight", "bus pass"],
		"rqSHOP Crystal Mall" : ["soup", "flashlight", "suitcase"]
	}
}

for room in rqdata.rooms.Room._registry:
	tmp = GenRoomJSON(room)
	gamedata['rooms'][tmp['name']] = tmp

gamedata['regions'] = GenRespawnJSON(rqdata.rooms.respawn,rqdata.rooms.rmessage)

gamedata['fast-travel'] = GenBusJSON(rqdata.rooms.busstops)

gamedata['costs'] = {
	"heal" : 20,
	"attack" : 0,
	"block" : 5
}

gamedata['dispensers'] = {
	"rooms" : {
		"fish" : ["UTP Office"],
		"fridge" : [*rqdata.rooms.respawn.values()]
	},
	"fish" : {
		"trash" : 750,
		"fish" : 150,
		"rare fish" : 90,
		"souper soup" : 10,
	},
	"fridge" : {
		"soup" : 50,
		"healthy soup" : 50,
		"salad" : 25,
		"battle soup" : 20,
		"souper soup" : 10
	}
}
with open("rqdata/extra_data.json", "r") as room_json:
	datadict = json.load(room_json)
	for key in datadict:
		gamedata[key] = datadict[key]

with open("rooms.json","w") as room_json:
	json.dump(gamedata,room_json,indent=2)
