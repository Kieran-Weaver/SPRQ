class Room(object):
  _registry = []
  
  def __init__(self, name, exits, dexits, info, npcs, region, spawner = None):
    self.name = name
    self.exits = exits
    self.dexits = dexits
    self.info = info
    self.npcs = npcs
    self.region = region
    self.spawner = spawner
    self._registry.append(self)

thunderbird_at_wesbrook = Room("Thunderbird at Wesbrook",
["none", "2900 Block Wesbrook Mall", "none", "Thunderbird Boulevard"],
None,
"You are at an intersection of a major north-south road and a small east-west road.",
["Squirrel", "Student"],
"South Campus")

thunderbird_boulevard = Room("Thunderbird Boulevard",
["none", "none", "Thunderbird at Wesbrook", "Thunderbird at East"],
None,
"You are on a short east-west road.",
["Squirrel", "Student"],
"South Campus")

thunderbird_at_east = Room("Thunderbird at East",
["none", "East Mall South", "Thunderbird Boulevard", "none"],
None,
"You are at the intersection of two small roads.",
["Squirrel", "Student"],
"South Campus")

wesbrook_mall_2900_block = Room("2900 Block Wesbrook Mall",
["Thunderbird at Wesbrook", "16th at Wesbrook", "none", "none"],
None,
"You are on the north section of a major north-south road. There is a bus stop here for\n\n25",
[],
"South Campus")

twenty_five = Room("25",
["none", "none", "none", "none", "UBC Bus Loop", "2900 Block Wesbrook Mall"],
None,
"You are on a bus running route 25. You can get to the following destinations:\n\nUBC Bus Loop\n2900 Block Wesbrook Mall",
[],
"South Campus")

east_mall_south = Room("East Mall South",
["Thunderbird at East", "16th at East", "Harry Warren Field", "none"],
None,
"You are on a small north-south road. To the east is a sports field.",
["Squirrel", "Student"],
"South Campus")

sixteenth_at_wesbrook = Room("16th at Wesbrook",
["2900 Block Wesbrook Mall", "3200 Block Wesbrook Mall", "none", "16th Avenue"],
None,
"You are at a roundabout leading out in 3 directions.",
["Squirrel", "Student"],
"South Campus")

sixteenth_avenue = Room("16th Avenue",
["none", "none", "16th at Wesbrook", "16th at East"],
None,
"You are on a short east-west road.",
["Squirrel", "Student"],
"South Campus")

sixteenth_at_east = Room("16th at East",
["East Mall South", "Ross Drive", "16th Avenue", "none"],
None,
"You are at a roundabout leading out in 3 directions.",
["Squirrel", "Student"],
"South Campus")

wesbrook_mall_3200_block = Room("3200 Block Wesbrook Mall",
["16th at Wesbrook", "Berton at Wesbrook", "none", "none"],
None,
"You are on the south section of a major north-south road.",
["Squirrel", "Student"],
"South Campus")

ross_drive = Room("Ross Drive",
["16th at East", "Berton at Ross", "UHill Parking Lot", "none"],
None,
"You are on a short north-south road. To the east is a parking lot.",
["Squirrel", "Student"],
"South Campus")

berton_at_wesbrook = Room("Berton at Wesbrook",
["3200 Block Wesbrook Mall", "none", "none", "Berton Avenue"],
None,
"You are at the intersection of a major north-south road and a small east-west road.",
["Squirrel", "Student"],
"South Campus")

berton_avenue = Room("Berton Avenue",
["none", "rqSHOP Wesbrook Village", "Berton at Wesbrook", "Berton at Ross"],
None,
"You are on a small east-west road. To the south is a shop.",
["Squirrel", "Student"],
"South Campus")

berton_at_ross = Room("Berton at Ross",
["Ross Drive", "none", "Berton Avenue", "none"],
None,
"You are at the intersection of 2 small roads.",
["Squirrel", "Student"],
"South Campus")

uhill_parking_lot = Room("UHill Parking Lot",
["none", "none", "UHill Hallway", "Ross Drive"],
None,
"You are in a school parking lot. To the west is a small road and to the east is a hallway.",
["Squirrel", "Student"],
"South Campus")

uhill_hallway = Room("UHill Hallway",
["none", "none", "UHill Cafeteria", "UHill Parking Lot"],
None,
"You are in a hallway. To the east is a cafeteria. To the west is a parking lot.",
["Student"],
"South Campus")

uhill_cafeteria = Room("UHill Cafeteria",
["none", "none", "none", "UHill Hallway"],
None,
"You are in a small cafeteria. There is a fridge here. To the west is a hallway.",
[],
"South Campus")

harry_warren_field = Room("Harry Warren Field",
["none", "none", "none", "East Mall South"],
None,
"You are in an expansive sports field. To the west is a small north-south road.",
["Soccer"],
"South Campus")

rqshop_wesbrook_village = Room("rqSHOP Wesbrook Village",
["Berton Avenue", "none", "none", "none"],
None,
"You are in a small trinket shop. To the north is Berton Avenue. There is a sign here that says:\n\nAvailable for free:💖\nAvailable for 100 coins:⚽\nAvailable for 1000000 coins:💸",
[],
"South Campus")

#--------------end of Episode 3 (south campus) rooms----------
