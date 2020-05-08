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

four_ten = Room("410",
["Gilley at Westminster", "Aberdeen Station"],
["none", "none", "none", "none"],
"You are in a bus running route 410. You can go to the following destinations:\n\nGilley at Westminster\nAberdeen Station",
[],
"Hamilton")

gilley_at_westminster = Room("Gilley at Westminster",
["none", "none", "Gilley Road West", "none"],
None,
"You are at an intersection of two roads. There is a bus stop here for\n\n410",
[],
"Hamilton")

gilley_road_west = Room("Gilley Road West",
["none", "none", "Gilley at Smith", "Gilley at Westminster"],
None,
"You are at the west side of a short east-west road.",
[],
"Hamilton")

gilley_at_smith = Room("Gilley at Smith",
["none", "none", "Gilley Road East", "Gilley Road West"],
None,
"You are at an intersection of two roads.",
[],
"Hamilton")

gilley_road_east = Room("Gilley Road East",
["none", "Hamilton Park Maze Entrance", "none", "Gilley at Smith"],
None,
"You are at the east side of a short east-west road. To the south is a park.",
[],
"Hamilton")

hamilton_park__maze_entrance = Room("Hamilton Park Maze Entrance",
["Gilley Road East", "h0", "none", "none"],
None,
"You are at the entrance to a small maze.",
[],
"Hamilton")


h0 = Room("h0",
["Hamilton Park Maze Entrance", "h1", "h11", "h2"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h1 = Room("h1",
["h25", "h9", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h2 = Room("h2",
["h25", "h25", "h0", "h47"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h3 = Room("h3",
["h25", "h4", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h4 = Room("h4",
["h3", "h6", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h5 = Room("h5",
["h25", "h25", "h6", "h25"],
None,
"You are in a park with many identical paths.",
["Programmer Redux"],
"Hamilton")

h6 = Room("h6",
["h4", "h25", "h7", "h5"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h7 = Room("h7",
["h25", "h25", "h8", "h6"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h8 = Room("h8",
["h9", "h25", "h22", "h7"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h9 = Room("h9",
["h25", "h25", "h21", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h10 = Room("h10",
["h11", "h25", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h11 = Room("h11",
["h25", "h10", "h12", "h0"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h12 = Room("h12",
["h25", "h25", "h13", "h11"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h13 = Room("h13",
["h25", "h25", "h15", "h12"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h14 = Room("h14",
["h25", "h15", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h15 = Room("h15",
["h14", "h16", "h25", "h13"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h16 = Room("h16",
["h15", "h19", "h17", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h17 = Room("h17",
["h25", "h25", "h25", "h16"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h18 = Room("h18",
["h25", "h25", "h19", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h19 = Room("h19",
["h16", "h20", "h25", "h18"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h20 = Room("h20",
["h19", "h23", "h25", "h21"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h21 = Room("h21",
["h25", "h22", "h20", "h9"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h22 = Room("h22",
["h21", "h25", "h24", "h8"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h23 = Room("h23",
["h20", "h24", "h33", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h24 = Room("h24",
["h23", "h27", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h25 = Room("h25",
["h25", "h26", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h26 = Room("h26",
["h25", "h25", "h27", "h1"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h27 = Room("h27",
["h14", "h25", "h28", "h26"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h28 = Room("h28",
["h29", "h25", "h40", "h27"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h29 = Room("h29",
["h30", "h28", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h30 = Room("h30",
["h31", "h29", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h31 = Room("h31",
["h25", "h30", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h32 = Room("h32",
["h25", "h31", "h34", "h33"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h33 = Room("h33",
["h25", "h25", "h32", "h23"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h34 = Room("h34",
["h35", "h25", "h25", "h32"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h35 = Room("h35",
["h36", "h34", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h36 = Room("h36",
["h25", "h37", "h35", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h37 = Room("h37",
["h38", "h25", "h39", "h36"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h38 = Room("h38",
["h25", "h37", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h39 = Room("h39",
["h25", "h25", "h47", "h37"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h40 = Room("h40",
["h25", "h25", "h41", "h28"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h41 = Room("h41",
["h42", "h25", "h25", "h40"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h42 = Room("h42",
["h44", "h41", "h43", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h43 = Room("h43",
["h25", "h25", "h25", "h42"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h44 = Room("h44",
["h25", "h42", "h25", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h45 = Room("h45",
["h25", "h25", "h46", "h43"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h46 = Room("h46",
["h47", "h25", "h3", "h45"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")

h47 = Room("h47",
["h25", "h46", "h2", "h25"],
None,
"You are in a park with many identical paths.",
[],
"Hamilton")
 
#----------end of Hamilton rooms and Episode 2 rooms---------
