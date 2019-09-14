npclist = ["Seagull", "Squirrel", "Pigeon", "Crow", "Diwheel", "Student", "Cookie", "Box Robot"]

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

six_hundred_one = Room("601",
["none", "none", "none", "none", "Bridgeport Station Bus Loop", "Ladner Exchange", "12 at 56"],
None,
"You are on a bus running route 601. You can disembark at:\n\nBridgeport Station Bus Loop\nLadner Exchange\n12 at 56",
[],
"Ladner")

ladner_exchange = Room("Ladner Exchange",
["none", "none", "none", "Harvest Drive"],
None,
"You are at a small loop with buses. There are bus stops here for:\n\n310\n601\n620",
[],
"Ladner")

harvest_drive = Room("Harvest Drive",
["Ladner Trunk at Harvest", "none", "Ladner Exchange", "none"],
None,
"You are on a short north-south road. To the east is a small loop with buses.",
["Seagull", "Squirrel"],
"Ladner")

ladner_at_harvest = Room("Ladner Trunk at Harvest",
["none", "Harvest Drive", "none", "Ladner Trunk Road E"],
None,
"You are at the intersection of a short north-south road and a long east-west road.",
["Seagull", "Squirrel"],
"Ladner")

ladner_trunk_e = Room("Ladner Trunk Road E",
["none", "none", "Ladner Trunk at Harvest", "Ladner Trunk at Linden"],
None,
"You are on the east section of a long east-west road.",
["Seagull", "Squirrel"],
"Ladner")

ladner_at_linden = Room("Ladner Trunk at Linden",
["Linden Drive", "none", "Ladner Trunk Road E", "Ladner Trunk Road W"],
None,
"You are at the intersection of a road leading north and a long east-west road.",
["Seagull", "Squirrel"],
"Ladner")

linden_drive = Room("Linden Drive",
["none", "Ladner Trunk at Linden", "none", "none"],
None,
"You are on a small roadway leading south.",
["Squirrel Army"],
"Ladner")

ladner_trunk_w = Room("Ladner Trunk Road W",
["none", "none", "Ladner Trunk at Linden", "Ladner Trunk at Arthur"],
None,
"You are on the west section of a long east-west road.",
["Seagull", "Squirrel"],
"Ladner")

ladner_at_arthur = Room("Ladner Trunk at Arthur",
["Elliott Street", "Magee Park", "Ladner Trunk Road W", "47A Avenue"],
None,
"You are at the intersection of four different roads leading in all directions.",
["Seagull", "Squirrel"],
"Ladner")

elliott_street = Room("Elliott Street",
["none", "Ladner Trunk at Arthur", "none", "none"],
None,
"You are on a small road leading south.",
["Ladner Programmer"],
"Ladner")

forty_seven_a = Room("47A Avenue",
["none", "none", "Ladner Trunk at Arthur", "none"],
None,
"You are on a small road leading east.",
["Seagull Flock Redux"],
"Ladner")

magee_park = Room("Magee Park",
["Ladner Trunk at Arthur", "none", "none", "none"],
None,
"You are at a small park. There is a fridge here.",
[],
"Ladner")

matthews_exchange = Room("Matthews Exchange",
["none", "none", "none", "none"],
None,
"You are at a small bus loop. There are bus stops here for:\n\n310\n351",
[],
"Ladner")

three_ten = Room("310", 
["none", "none", "none", "none", "Ladner Exchange", "Matthews Exchange"],
None,
"You are on a bus running route 310. You can disembark at:\n\nLadner Exchange\nMatthews Exchange",
[],
"Ladner")

#------------------end of ladner rooms----------------------
sdrc = Room("South Delta Recreation Centre",
["none", "none", "none", "56 Street N"],
None,
"You are at a rec centre. There is a fridge here.",
[],
"Tsawwassen")

fifty_six_north = Room("56 Street N",
["none", "16 at 56", "South Delta Recreation Centre", "none"],
None,
"You are on the north section of a central north-south road.",
["Squirrel", "Seagull"],
"Tsawwassen")

sixteen_at_56 = Room("16 at 56", 
["56 Street N", "56 Street S", "none", "16 Avenue"],
None,
"You are at the intersection of a road leading west and a north-south road.",
["Squirrel", "Seagull"],
"Tsawwassen")

sixteen_avenue = Room("16 Avenue",
["none", "none", "16 at 56", "none"],
None,
"You are on a small road leading east.",
["Tsawwassen Programmer"],
"Tsawwassen")

fifty_six_south = Room("56 Street S",
["16 at 56", "12 at 56", "none", "none"],
None,
"You are on the south section of a central north-south road.",
["Squirrel", "Seagull"],
"Tsawwassen")

twelve_at_56 = Room("12 at 56",
["56 Street S", "none", "12 Avenue E", "12 Avenue W"],
None,
"You are at the intersection of a road leading north and an east-west road. There is a bus stop here for:\n\n601",
[],
"Tsawwassen")

twelve_w = Room("12 Avenue W",
["none", "none", "12 at 56", "none"],
None,
"You are on a road leading east.",
["Flying Doge Redux"],
"Tsawwassen")

twelve_e = Room("12 Avenue E",
["none", "none", "none", "12 at 56"],
None,
"You are on a road leading west.",
["Obsessed Comic Fan Redux"],
"Tsawwassen")

tft = Room("Tsawwassen Ferry Terminal",
["none", "none", "none", "none"],
None,
"You are at the Tsawwassen Ferry Terminal. There is a bus stop here for:\n\n620",
[],
"Tsawwassen")

six_twenty = Room("620",
["none", "none", "none", "none", "Ladner Exchange", "Tsawwassen Ferry Terminal"],
None,
"You are on a bus running route 620. You can disembark at:\n\nLadner Exchange\nTsawwassen Ferry Terminal",
[],
"Tsawwassen")

#----------------end of tsawwassen rooms----------------------

southmere_park = Room("Southmere Village Park",
["none", "North Bluff Road", "none", "none"],
None,
"You are at a small park with lakes. There is a fridge here.",
[],
"White Rock")

north_bluff_road = Room("North Bluff Road",
["Southmere Village Park", "none", "North Bluff at 152", "none"],
None,
"You are on a small east-west road.",
["Seagull"],
"White Rock")

three_fifty_one = Room("351",
["none", "none", "none", "none", "Matthews Exchange", "North Bluff at 152", "Sullivan Street E"],
None,
"You are on a bus running route 351. You can disembark at:\n\nSullivan Street E\nNorth Bluff at 152\nMatthews Exchange",
[],
"White Rock")

north_bluff_at_152 = Room("North Bluff at 152",
["152 Street S", "Johnston Street", "none", "North Bluff Road"],
None,
"You are at the intersection of a north-south road and a small road leading west. There is a bus stop here for:\n\n351",
[],
"White Rock")

johnston_street = Room("Johnston Street",
["North Bluff at 152", "none", "none", "none"],
None,
"You are on a short road leading north to a different north-south road.",
["Raccoon"],
"White Rock")

one_fifty_second_s = Room("152 Street S",
["18 at 152", "North Bluff at 152", "none", "none"],
None,
"You are on the south section of a central north-south road.",
["Seagull"],
"White Rock")

eighteen_at_152 = Room("18 at 152",
["152 Street N", "152 Street S", "18 Avenue", "none"],
None,
"You are at the intersection of a north-south road and a road leading east.",
["Seagull"],
"White Rock")

one_fifty_second_n = Room("152 Street N",
["none", "18 at 152", "none", "none"],
None,
"You are on a central road leading south.",
["Leaf Pile Redux"],
"White Rock")

eighteen_avenue = Room("18 Avenue",
["Bakerview Park", "none", "none", "18 at 152"],
None,
"You are on a road leading west. To the north is a park.",
["Seagull"],
"White Rock")

bakerview_park = Room("Bakerview Park",
["none", "18 Avenue", "none", "none"],
None,
"You are at a small park.",
["White Rock Programmer"],
"White Rock")

#-----------------end of white rock rooms--------------------

sullivan_street_e = Room("Sullivan Street E",
["none", "none", "Sullivan at Kidd", "Sullivan at McBride"],
None,
"You are at the east section of an east-west road. There is a fridge on a bench here. There is a bus stop here for:\n\n351",
[],
"Crescent Beach")

sullivan_at_kidd = Room("Sullivan at Kidd",
["none", "none", "none", "Sullivan Street E"],
None,
"You are at the intersection of two roads, one of which leads west.",
["Crescent Beach Programmer"],
"Crescent Beach")

sullivan_at_mcbride = Room("Sullivan at McBride",
["McBride Avenue N", "McBride Avenue S", "Sullivan Street E", "Sullivan Street W"],
None,
"You are at an intersection leading in all directions.",
["Seagull"],
"Crescent Beach")

mcbride_n = Room("McBride Avenue N",
["none", "Sullivan at McBride", "none", "none"],
None,
"You are on a short road leading south.",
["Pelican"],
"Crescent Beach")

mcbride_s = Room("McBride Avenue S",
["Sullivan at McBride", "none", "none", "none"],
None,
"You are on a short road leading north.",
["Pelican Redux"],
"Crescent Beach")

sullivan_street_w = Room("Sullivan Street W",
["none", "none", "Sullivan at McBride", "Crescent Beach Entrance"],
None,
"You are at the west section of an east-west road. To the east is a beach.",
["Seagull"],
"Crescent Beach")

crescent_beach_entrance = Room("Crescent Beach Entrance",
["none", "none", "Sullivan Street W", "c0"],
None,
"You are at the entrance to a beach. It is locked. There are four circular indents on the door.",
["Seagull"],
"Crescent Beach")

#------------------Crescent Beach Maze Below------------------

c0 = Room("c0",
["c4", "none", "Crescent Beach Entrance", "c1"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c1 = Room("c1",
["none", "none", "c0", "c2"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c2 = Room("c2",
["c3", "c1", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c3 = Room("c3",
["none", "c2", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c4 = Room("c4",
["c5", "none", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c5 = Room("c5",
["c6", "c4", "c8", "c7"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c6 = Room("c6",
["none", "c5", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
["Programmer_Redux_Redux"],
"Crescent Beach")

c7 = Room("c7",
["c12", "none", "c5", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c8 = Room("c8",
["c9", "none", "none", "c5"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c9 = Room("c9",
["c10", "c8", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c10 = Room("c10",
["none", "c9", "none", "c11"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c11 = Room("c11",
["c13", "c12", "c10", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c12 = Room("c12",
["c11", "c7", "none", "c14"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c13 = Room("c13",
["none", "c11", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c14 = Room("c14",
["none", "none", "c12", "c15"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c15 = Room("c15",
["c16", "none", "c14", "c17"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c16 = Room("c16",
["none", "c15", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c17 = Room("c17",
["none", "c18", "c15", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c18 = Room("c18",
["c17", "c19", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c19 = Room("c19",
["c18", "c25", "c20", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c20 = Room("c20",
["none", "c21", "none", "c19"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c21 = Room("c21",
["c20", "c22", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c22 = Room("c22",
["c21", "c23", "c31", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c23 = Room("c23",
["c22", "c24", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c24 = Room("c24",
["c23", "c25", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c25 = Room("c25",
["c24", "c16", "c26", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c26 = Room("c26",
["c27", "c13", "c37", "c25"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c27 = Room("c27",
["none", "c26", "c28", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c28 = Room("c28",
["c29", "c37", "none", "c27"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c29 = Room("c29",
["none", "c28", "none", "c30"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c30 = Room("c30",
["c31", "none", "c29", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c31 = Room("c31",
["none", "c30", "c22", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")

c32 = Room("c32",
["none", "none", "none", "none"],
None,
"You are at Crescent Beach. Everything is covered in snow.",
npclist,
"Crescent Beach")
