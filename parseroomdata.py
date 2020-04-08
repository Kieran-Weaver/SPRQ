import re
import os
import json
import ast
import string
import collections
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
		roomdict['spawner'] = literal_room[6]
	except:
		roomdict['spawner'] = None
	return (PrintRoom(roomdict),roomdict)

def GenRespawnJSON(spawnpoints,rmessages):
	regions = spawnpoints.keys()
	rdata = {}
	for key in regions:
		rdata[key] = {'room':spawnpoints[key],'message':rmessages[key]}
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
	'respawn' : {
	},
	'fast-travel' : {
	},
	'players' : {
	},
	'npcs' : {
		"Diwheel": {
			"name" : "DiWheel",
			"hp" : 20,
			"atk" : 1,
			"def" : 0,
			"xp" : 1,
			"text": {
				"entry" : "Jim is in the room, driving his DiWheel robot towards you",
				"turn" : "DiWheel used quick attack! It isn't very effective",
				"win" : "I think I heard Irena scream in the distance",
				"lose" : "You blacked out! Jim put your body in a sleeping bag and mailed you home."
			},
			"money" : 5,
			"drops" : {
				"soup" : 16
			}
		},
		"Box Robot": {
			"name" : "Box Robot",
			"hp" : 10,
			"atk" : 4,
			"def" : 0,
			"xp" : 5,
			"text": {
				"entry" : "There is a box-shaped robot on the floor.\n It's staring at you menacingly",
				"turn" : "The robot charges at you and tries to knock you down",
				"win" : "The robot violently exploded. Nice.",
				"lose" : "You blacked out! The robot taunts you, spinning in circles"
			},
			"money" : 5,
			"drops" : {
				"soup" : 16
			}
		},
		"Student": {
			"name" : "Student",
			"hp" : 40,
			"atk" : 2,
			"def" : 0,
			"xp" : 20,
			"text": {
				"entry": "Tobias fell out of the sky and his arms returned to their normal size.",
				"turn": "Tobias shot lightning at you, but you are wearing a metal jacket",
				"win": "You're already a better fighter than most of the Agency",
				"lose": """ "You're still so weak, Laura," Tobias said """
			},
			"money" : 10,
			"drops" : {
				"soup" : 16
			}
		},
		"Seagull": {
			"name" : "Seagull",
			"hp" : 5,
			"atk" : 8,
			"def" : 2,
			"xp" : 2,
			"text": {
				"entry": "A seagull decided you tasted better than some guy's fries.",
				"turn": "Birds are jerks! It rammed right into your face",
				"win": "Now you can have lunch in peace",
				"lose": "You blacked out!"
			},
			"money" : 20,
			"drops" : {
				"soup" : 16
			}
		},
		"Pigeon": {
			"name" : "Pidgeon",
			"hp" : 60,
			"atk" : 10,
			"def" : 0,
			"xp" : 20,
			"text": {
				"entry": "You're approaching me?",
				"turn": "Instead of running away, you're coming closer?",
				"win": "Why are all the bosses birds, anyway",
				"lose": "This isn't a pidgeon! It's me, DIO!"
			},
			"money" : 25,
			"drops" : {
				"soup" : 16
			}
		},
		"Crow": {
			"name" : "Crow",
			"hp" : 100,
			"atk" : 15,
			"def" : 0,
			"xp" : 40,
			"text": {
				"entry": "There's a crow the size of a cow sitting in front of you",
				"turn": "It attempted to crush you under its massive weight",
				"win": "Stop this animal abuse!",
				"lose": "You blacked out! Wait until items are implemented next time"
			},
			"money" : 50,
			"drops" : {
				"soup" : 16
			}
		},
		"Cookie": {
			"name" : "Cookie",
			"hp" : 2,
			"atk" : 255,
			"def" : 0,
			"xp" : 0,
			"text": {
				"entry": "It's a cookie, how tough could it be?",
				"turn": "IT GREW FOUR HUNDRED EYES AND THEY ALL STARED AT YOU",
				"win": "See? Good thing you defeated it quickly...",
				"lose": "You blacked out and it bit you as revenge"
			},
			"money" : 1,
			"drops" : {
				"soup" : 16
			}
		}
	},
	"items" : {
		'soup' : {
			'type' : 'any',
			'cost' : 1,
			'hp' : 0,
			'sp' : 10,
			'atk' : 0
		},
		'health_soup' : {
			'type' : 'any',
			'cost' : 10,
			'hp' : 10,
			'sp' : 0,
			'atk' : 0
		},
		'souper_soup' : {
			'type' : 'any',
			'cost' : 20,
			'hp' : 50,
			'sp' : 50,
			'atk' : 1
		},
		'battle_soup' : {
			'type' : 'battle',
			'cost' : 10,
			'atk' : 10
		},
		'bus_pass' : {
			'type' : 'powerup',
			'cost' : 25
		},
		'repel' : {
			'type' : 'powerup',
			'cost' : 50
		},
		'flashlight' : {
			'type' : 'special',
			'atk' : 10,
			'cost' : 50
		},
		'bag' : {
			'type' : 'powerup',
			'data' : 20,
			'cost' : 100
		},
		'lock' : {
			'type' : 'powerup',
			'data' : 20,
			'cost' : 200
		},
		'suitcase' : {
			'type' : 'powerup',
			'data' : 100,
			'cost' : 500
		},
		'satellite' : {
			'type' : 'powerup',
			'data' : 0,
			'cost' : 1000
		}
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

gamedata['respawn'] = GenRespawnJSON(respawnlists[0],respawnlists[1])

gamedata['fast-travel'] = GenBusJSON(ast.literal_eval(busdata))

with open("rooms.json","w") as room_json:
	json.dump(gamedata,room_json,indent=2)
	
