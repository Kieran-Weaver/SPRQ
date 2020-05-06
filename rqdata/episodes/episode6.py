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

vancouver_nanaimo_ferry = Room("Vancouver-Nanaimo Ferry",
["none", "none", "none", "none", "Nanaimo Ferry Terminal", "Tsawwassen Ferry Terminal"],
None,
"You are in a ferry running the Vancouver-Nanaimo route. You can go to the following destinations:\n\nNanaimo Ferry Terminal\nTsawwassen Ferry Terminal",
[],
"Nanaimo")

bamfield_shuttle = Room("Bamfield Shuttle",
["none", "none", "none", "none", "Nanaimo", "Pachena Road"],
None,
"You are in a bus running the Bamfield Shuttle. You can go to the following destinations:\n\nNanaimo\nPachena Road",
[],
"Nanaimo")

nanaimo = Room("Nanaimo",
["Nanaimo Ferry Terminal", "none", "none", "none"], 
None,
"You are in Nanaimo. There is a bus stop here for\n\nBamfield Shuttle.",
[],
"Nanaimo")

nanaimo_ferry_terminal = Room("Nanaimo Ferry Terminal",
["none", "Nanaimo", "none", "none"],
None,
"You are at the Nanaimo Ferry Terminal. There is a fridge here.",
[],
"Nanaimo")

#-------------------end of nanaimo rooms------------------

pachena_road = Room("Pachena Road",
["Bamfield Marine Sciences Centre Entrance", "none", "Bamfield Cafeteria Entrance", "Rix Centre Lounge", "Bamfield Roundabout"],
None,
"You are on a long gravel road with buildings in the north, east, and west.",
[],
"Bamfield")

rix_lounge = Room("Rix Centre Lounge",
["none", "none", "Pachena Road", "Rix Centre Hallway"],
None,
"You are in a large lounge with many couches. You can see a long hallway.",
["Seagull", "Student"],
"Bamfield")

rix_hallway = Room("Rix Centre Hallway",
["none", "none", "Rix Centre Lounge", "Rix Centre Classroom"],
None,
"You are in a long hallway between a classroom and a lounge.",
["Student", "Seagull"],
"Bamfield")

rix_classroom = Room("Rix Centre Classroom",
["none", "none", "Rix Centre Hallway", "none"],
None,
"You are in a classroom with many chairs and a projector.",
[],
"Bamfield")

bmsc_entrance = Room("Bamfield Marine Sciences Centre Entrance",
["Bamfield Marine Sciences Centre", "Pachena Road", "Whale Lab", "Dock Pathway S", "Bamfield Roundabout"],
None,
"You are in front of the Bamfield Marine Sciences Centre",
["Seagull", "Student"],
"Bamfield")

bmsc = Room("Bamfield Marine Sciences Centre",
["Bamfield Marine Sciences Centre Library", "Bamfield Marine Sciences Centre Entrance", "Bamfield Marine Sciences Centre Downstairs Hallway", "Bamfield Marine Sciences Centre Fishtanks"],
None,
"You are in the main Bamfield building",
["Seagull", "Student"],
"Bamfield")

bmsc_library = Room("Bamfield Marine Sciences Centre Library",
["none", "Bamfield Marine Sciences Centre", "none", "none"],
None,
"You are in a library. There are books here. There is an exit to the south",
["Seagull", "Student"],
"Bamfield")

bamfield_roundabout = Room("Bamfield Roundabout",
["Bamfield Marine Sciences Centre Entrance", "Pachena Road", "none", "none"],
None,
"You are on a small roundabout with a large tree.",
[],
"Bamfield")

bmsc_fishtanks = Room("Bamfield Marine Sciences Centre Fishtanks",
["none", "none", "Bamfield Marine Sciences Centre", "none", "hidden exit", "hidden exit"],
None,
"You are in a circular room. There are fishtanks with fish and pictures depicting Bamfield’s history.",
["Student", "Seagull"],
"Bamfield")

bmsc_downstairs = Room("Bamfield Marine Sciences Centre Downstairs Hallway",
["Bamfield Marine Sciences Centre Computer Lab", "none" "Bamfield Marine Sciences Centre Kelp Lab", "Dock Pathway N"],
None,
"You are in a hallway with many rooms and an exit at one end.",
["Student", "Seagull"],
"Bamfield")

bmsc_kelp = Room("Bamfield Marine Sciences Centre Kelp Lab",
["none", "none", "none", "Bamfield Marine Sciences Centre Downstairs Hallway"],
None,
"You are in a lab with an abundance of kelp growing.",
[], #can has some activity here
"Bamfield")

bmsc_computer = Room("Bamfield Marine Sciences Centre Computer Lab",
["none", "Bamfield Marine Sciences Centre Downstairs Hallway", "none", "none"],
None,
"You are in a computer lab with lots of computers.", 
["Student", "Seagull"],
"Bamfield")

dock_pathway_s = Room("Dock Pathway S",
["Dock Pathway N", "none", "Bamfield Marine Sciences Centre Entrance", "none"],
None,
"You are on a long thin path.",
["Seagull", "Student"],
"Bamfield")

dock_pathway_n = Room("Dock Pathway N",
["Water", "Dock Pathway S", "Bamfield Marine Sciences Centre Downstairs Hallway", "Bamfield Docks"],
None,
"You are on a long thin path. To the north is water, to the east is Bamfield Marine Sciences Centre, and to the west is a shed",
["Seagull", "Student"],
"Region of Room")

bamfield_docks = Room("Bamfield Docks",
["Water Maze Entrance", "Water", "Dock Pathway N", "Water"], #only enter water maze entrance if u have a boat, otherwise u die instantly
None,
"You are on the Bamfield Docks. Across the water you can see West Bamfield.", #you can buy boats here
["Seagull", "Student"],
"Bamfield")

water = Room("Water",
["Water", "Water", "Water", "Water", "Bamfield Docks"],
None,
"You are in water. Everywhere is water.", #instantly kill them if they don’t have a boat
[],
"Bamfield")

whale_lab = Room("Whale Lab",
["none", "none", "none", "Bamfield Marine Sciences Entrance"],
None,
"You are in the whale lab. There is a skeleton of a whale here, among other animals. There are tanks with a variety of marine creatures.",
["Seagull", "Student"],
"Bamfield")

bamfield_cafeteria_entrance = Room("Bamfield Cafeteria Entrance",
["Bamfield Cafeteria Lounge", "none", "Bamfield Cafeteria", "Pachena Road"],
None,
"You are at the entrance to the cafeteria.",
["Seagull", "Student"],
"Bamfield")

bamfield_cafeteria = Room("Bamfield Cafeteria",
["none", "none", "none", "Bamfield Cafeteria Entrance"],
None,
"You are in a room with many tables and chairs, along with food. There is a fridge here.",
[], #spawn
"Bamfield")

bamfield_cafeteria_lounge = Room("Bamfield Cafeteria Lounge",
["none", "Bamfield Cafeteria Entrance", "none", "none"],
None,
"You are in a room with couches and board games. There is a piano here.",
[], #can have a boss here or a game where u play the piano
"Bamfield")

