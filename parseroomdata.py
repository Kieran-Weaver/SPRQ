import re
import os
import json
import ast
import string
import collections
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
	"📇" : "bus_pass",
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
def PrintRoom(roomdict):
	numbers = ['zero','one','two','three','four','five','six','seven','eight','nine']
	roomname = re.sub(' ','_',roomdict['name']).lower()
	roomname = re.sub('^([0-9]+)',lambda match: ''.join([numbers[int(x)] for x in match.group(1)]),roomname)
	printable = set(string.printable)
	roomname = "".join([x for x in roomname if x in printable])
	keys = ['name','exits','info','npcs','region']
	roomstr = ''
	roomstr += roomname
	roomstr += ' = Room('
	for i in keys:
		roomstr += repr(roomdict[i])
		roomstr += ',\n'
	roomstr += repr(roomdict['spawner'])
	roomstr += ')'
	return roomstr
		
def GenRoomJSON(room):
	roomdict = {
		'name' : '',
		'exits': [],
		'info' : '',
		'npcs' : [],
		'region': '',
		'spawner': '',
#		'players': []
		'items' : []
	}
	literal_room = ast.literal_eval(room)
	new_exits = []
	if literal_room[2] != None:
		exits = set(literal_room[1])
		dexits = set(literal_room[2])
		new_exits = exits - dexits
		literal_room[2].extend(list(new_exits))
		roomdict['exits'] = literal_room[2]
	else:
		roomdict['exits'] = literal_room[1]
	roomdict['name'] = literal_room[0]
	roomdict['info'] = literal_room[3]
	roomdict['npcs'] = literal_room[4]
	roomdict['region'] = literal_room[5]
	roomdict['items'] = []
	try:
		roomdict['spawner'] = itemtable[literal_room[6]]
	except:
		roomdict['spawner'] = None
	return (PrintRoom(roomdict),roomdict)

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

roomdata = ""
auxdata = ""
#npclist = '["Box Robot", "Student", "Seagull", "Pigeon", "Crow", "Cookie", "Diwheel"]'
with open("rqdata/episodes/episode1.py",'r') as room_file:
    roomdata += '\n\n'
    roomdata += room_file.read()
    npclist_match = re.search('npclist = (\[.*\])',roomdata)
    roomdata = re.sub(r'npclist,',str(npclist_match.group(1))+',',roomdata)


with open("rqdata/rooms.py",'r') as room_file:
    auxdata = room_file.read()

roomdata = re.sub(r'npclist = (\[.*\])','',roomdata)
busdata = auxdata
respawndata = auxdata
roomdata = re.sub(r'.*utp_lounge','utp_lounge',roomdata,count=1,flags=re.DOTALL)
roomdata = re.sub(r'busstops = .*','',roomdata,count=1,flags=re.DOTALL)
roomdata = re.sub(r'#.*','',roomdata)
roomdata = re.sub(r"'''.*'''",'',roomdata,flags=re.DOTALL)

busdata = re.sub(r'.*busstops = ','',busdata,flags = re.DOTALL)
busdata = re.sub(os.linesep + 'respawn.*','',busdata,flags=re.DOTALL)

respawndata = re.sub('.*' + os.linesep + 'respawn = ','',respawndata,flags=re.DOTALL)
respawndata = re.sub(r'def findroom.*','',respawndata,flags=re.DOTALL)
respawnlists = [ast.literal_eval(x) for x in respawndata.split(os.linesep + 'rmessage = ')]

rooms = list(collections.OrderedDict.fromkeys(roomdata.split(os.linesep + os.linesep)))
rooms = [s for s in rooms if not "class Room" in s]
rooms = [re.sub(r'.*= Room','',room.strip(),flags=re.DOTALL) for room in rooms if room.strip()]
#rooms = [re.sub(r'npclist',npclist,room) for room in rooms]
rooms = [re.sub(r'\(','[',room) for room in rooms]
rooms = [re.sub(r'"\)','"]',room) for room in rooms]
rooms = [re.sub(r'\n','',room) for room in rooms]
rooms = [re.sub(r'"\+"\\n"\.join\[([^\)]*)\)',lambda match: eval('"\\\\n".join(' + match.group(1) + ')') + '\"', room) for room in rooms]

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
		"UBC Bookstore" : ["soup", "health_soup", "souper_soup", "flashlight", "bus_pass"],
		"YuBot Gift Shop Downtown Vancouver" : ["soup", "souper_soup", "flashlight", "bus_pass"],
		"YuBot Gift Shop Granville Island" : ["soup", "souper_soup", "flashlight", "bus_pass"],
		"YuBot Gift Shop False Creek South" : ["soup", "souper_soup", "flashlight", "bus_pass"],
		"rqSHOP False Creek South" : ["satellite"],
		"RQ Storage Solutions False Creek South" : ["bag", "suitcase"],
		"YuBot Gift Shop Kerrisdale" : ["soup", "souper_soup", "flashlight", "bus_pass"],
		"rqSHOP Kerrisdale" : ["repel"],
		"YuBot Gift Shop Brighouse" : ["soup", "souper_soup", "flashlight", "bus_pass"],
		"rqSHOP Brighouse" : ["lock", "suitcase", "sattelite"],
		"rqSHOP Wesbrook Village" : ["soup", "souper_soup", "battle_soup", "health_soup"],
		"YuBot Gift Shop Commercial-Broadway" : ["soup", "souper_soup", "flashlight", "bus_pass"],
		"YuBot Gift Shop Crystal Mall" : ["soup", "souper_soup", "flashlight", "bus_pass"],
		"rqSHOP Crystal Mall" : ["soup", "flashlight", "suitcase"]
	}
}
with open("fullrooms.py","w") as fullroomfile:
	fullroomfile.write("""class Room(object):
  _registry = []
  
  def __init__(self, name, exits, info, npcs, region, spawner = None):
    self.name = name
    self.exits = exits
    self.info = info
    self.npcs = npcs
    self.region = region
    self.spawner = spawner
    self._registry.append(self)
    
""")
	for room in rooms:
		tmp = GenRoomJSON(room)
		gamedata['rooms'][tmp[1]['name']] = tmp[1]
		fullroomfile.write(tmp[0])
		fullroomfile.write('\n\n')

gamedata['regions'] = GenRespawnJSON(respawnlists[0],respawnlists[1])

gamedata['fast-travel'] = GenBusJSON(ast.literal_eval(busdata))

gamedata['costs'] = {
	"heal" : 20,
	"attack" : 0,
	"block" : 5
}

gamedata['dispensers'] = {
	"rooms" : {
		"fish" : ["UTP Office"],
		"fridge" : [*respawnlists[0].values()]
	},
	"fish" : {
		"trash" : 750,
		"fish" : 150,
		"rare fish" : 90,
		"souper_soup" : 10,
	},
	"fridge" : {
		"soup" : 50,
		"healthy soup" : 50,
		"salad" : 25,
		"battle soup" : 20,
		"souper_soup" : 10
	}
}
with open("rqdata/npcs.json", "r") as room_json:
	npcdict = json.load(room_json)
	gamedata["items"] = npcdict["items"]
	gamedata["npcs"] = npcdict["npcs"]
	gamedata["bosses"] = npcdict["bosses"]

with open("rooms.json","w") as room_json:
	json.dump(gamedata,room_json,indent=2)
