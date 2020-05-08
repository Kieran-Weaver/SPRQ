import os
import importlib

class Room(object):
  _registry = []
  for fname in os.listdir("rqdata/episodes"):
    if fname.endswith(".py"):
      fname = fname.replace(".py", "")
      ep = importlib.import_module(f"rqdata.episodes.{fname}")
      _registry.extend(ep.Room._registry)

  def __init__(self, name, exits, dexits, info, npcs, region, spawner = None):
    self.name = name
    self.exits = exits
    self.dexits = dexits
    self.info = info
    self.npcs = npcs
    self.region = region
    self.spawner = spawner
    self._registry.append(self)

def findroom(name):
  for room in Room._registry:
    if room.name == name:
      return room
  return None

busstops = {
	"Memorial at West":["68"],
	"UBC Bus Loop":["25", "43", "44", "68", "84", "99", "480"],
	"Waterfront Station":["44", "10", "Canada Line", "Expo Line"],
	"Pender at Granville":["19"],
	"Georgia at Granville":["250"],
	"Georgia at Homer":["250"],
	"Robson at Granville":["10"],
	"Hastings at Granville":["10"],
	"Vancouver City Centre Station":["Canada Line"],
	"5th at Granville":["10"],
	"Lamey's Mill at Anderson":["50"],
	"4th at Fir":["84"],
	"Olympic Village Station":["Canada Line"],
	"500 Block 2nd Avenue":["50", "84"],
	"Broadway at Cambie":["99"],
	"Commercial-Broadway Station":["99", "Expo Line"],
	"Broadway-City Hall Station":["Canada Line"],
	"41st at Granville":["10", "43"],
	"41st at West Boulevard":["43"],
	"41st at Cambie":["43"],
	"Oakridge-41st Station":["Canada Line"],
	"Marine Drive Station":["Canada Line"],
	"Marine at Cambie":["10"],
	"Pipeline at Stanley Park":["19"],
	"Stanley Park Loop":["19"],
	"Bridgeport Station Bus Loop":["480", "403", "601"],
	"Bridgeport Station":["Canada Line"],
	"Entertainment Roundabout":["403"],
	"Lansdowne at No. 3":["403"],
	"Westminster at No. 3":["403"],
	"Cook at No. 3":["403"],
	"Granville at No. 3":["403"],
	"Lansdowne Station":["Canada Line"],
	"Brighouse Station":["Canada Line"],
	"Aberdeen Station":["Canada Line", "403", "410"],
	"Gilley at Westminster":["410"],
	"2900 Block Wesbrook Mall":["25"],
	"Ladner Exchange":["310", "601" ,"620"],
	"12 at 56":["601"],
	"Tsawwassen Ferry Terminal":["620", "Vancouver-Nanaimo Ferry"],
	"Matthews Exchange":["310", "351"],
	"North Bluff at 152":["351"],
	"Sullivan Street E":["351"],
	"Joyce-Collingwood Station":["43", "Expo Line"],
	"Patterson Station":["Expo Line"],
	"Metrotown Station":["19", "119", "144", "430"],
	"Edmonds Station":["106", "119", "Expo Line"],
	"Kingsway at Griffiths":["119"],
	"Edmonds at Kingsway":["106", "119"],
	"New Westminster Station":["106", "Expo Line"], # and others
  "Nanaimo Ferry Terminal":["Vancouver-Nanaimo Ferry"],
  "Nanaimo":["Bamfield Shuttle"]
}

respawn = {
	"UBC":"UTP Lounge",
	"Downtown Vancouver":"Robson Square",
	"Granville Island":"Granville Island Public Market",
	"False Creek South":"Olympic Village Station",
	"41st @ Granville":"Food Cart 41st/Granville",
	"Kerrisdale":"Arbutus Greenway",
	"Oakridge":"Oakridge-41st Station",
	"Marine Drive":"Marine Drive Station",
	"Stanley Park":"Stanley Park Loop",
	"Bridgeport":"Bridgeport Station",
	"Riverport":"Theatres",
	"Brighouse":"Richmond Public Library Brighouse Branch",
	"Hamilton":"UTP Lounge",
	"South Campus":"UHill Cafeteria",
	"Ladner":"Magee Park",
	"Tsawwassen":"South Delta Recreation Centre",
	"White Rock":"Southmere Village Park",
	"Crescent Beach":"Sullivan Street E",
	"Commercial-Broadway":"Commercial-Broadway Station",
	"Metrotown":"Central Park Path​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​​",
	"Edmonds":"Highgate Supermarket",
  "New West":"Highgate Supermarket",
	#"New Westminster":"Royal City Mall" probably
  "Nanaimo":"Nanaimo Ferry Terminal",
  "Bamfield":"Bamfield Cafeteria"
}

rmessage = {
	"UBC":" When you wake up, you find yourself back in the small room with tables and a fridge. Your pockets are empty.",
	"Downtown Vancouver":" When you wake up, you find yourself back in the expansive patio with tables and a fridge. Your pockets are empty.",
	"Granville Island":" When you wake up, you find yourself back in the Granville Island market with the free samples cart. Your pockets are empty.",
	"False Creek South":" When you wake up, you find yourself back in the Canada Line station with the info table and fridge. Your pockets are empty.",
	"41st @ Granville":" When you wake up, you find yourself back at the food cart with a fridge. Your pockets are empty.",
	"Kerrisdale":" When you wake up, you find yourself back at the wide path with tables and a fridge. Your pockets are empty.",
	"Oakridge":" When you wake up, you find yourself back in the Canada Line station with the info table and fridge. Your pockets are empty.",
	"Marine Drive":" When you wake up, you find yourself back in the Canada Line station with the info table and fridge. Your pockets are empty.",
	"Stanley Park":" When you wake up, you find yourself back in the small bus loop with a pavilion and fridge. Your pockets are empty.",
	"Bridgeport":" When you wake up, you find yourself back in the Canada Line station with the info table and fridge. Your pockets are empty.",
	"Riverport":" When you wake up, you find yourself back at the movie theatre. Your pockets are empty.",
	"Brighouse":" When you wake up, you find yourself back in the library with a fridge. Your pockets are empty.",
	"Hamilton":" When you wake up, you find yourself back in the small room with tables and a fridge. Your pockets are empty.",
	"South Campus":" When you wake up, you find yourself back in the cafeteria with a fridge. Your pockets are empty.",
	"Ladner":" When you wake up, you find yourself back in the small park with a nearby fridge. Your pockets are empty.",
	"Tsawwassen":" When you wake up, you find yourself back in the rec centre with a fridge. Your pockets are empty.",
	"White Rock":" When you wake up, you find yourself back in the park with two lakes and a nearby fridge. Your pockets are empty.",
	"Crescent Beach":"When you wake up, you find yourself back in the east section of an east-west road. Your pockets are empty.",
	"Commercial-Broadway":" When you wake up, you find yourself back in the busy SkyTrain station with a food cart. Your pockets are empty.",
	"Metrotown":" When you wake up, you find yourself back in the park path with a fridge. Your pockets are empty.",
	"Edmonds":" When you wake up, you find yourself back in the supermarket with a fridge. Your pockets are empty.",
  "New West":" When you wake up, you find yourself back in the supermarket with a fridge. Your pockets are empty.",
  "Nanaimo":" When you wake up, you find yourself back in the ferry terminal with a fridge. Your pockets are empty.",
  "Bamfield":" When you wake up, you find yourself back in the cafeteria with a fridge. Your pockets are empty."
}
