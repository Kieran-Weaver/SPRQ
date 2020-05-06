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

utp_lounge = Room("UTP Lounge", 
["UTP Office", "UTP Hallway", "none", "UTP Lockers"], 
"Try `>open fridge`",
"You are standing in a small room with some tables in the middle. To the south is a small hallway, and to the west is a series of lockers.\n\nThere is a fridge here.\nThere is a TV here.", 
[], 
"UBC")

utp_lockers = Room("UTP Lockers", 
["none", "none", "UTP Lounge", "UTP Balcony"],
"Try `>get 🔦 from locker` or `>open locker`", 
"You are in front of a wall of lockers. They are all locked. There is one with your name on it which you happen to know the password to. To the west is a balcony and to the east is a small room.", 
[], 
"UBC")

utp_office = Room("UTP Office", 
["none", "UTP Lounge", "none", "none"],
"Try `>fish`", 
"You are in a tiny office outside the small room. There are numerous computers stored to one side. One of them has a virtual fishing game running. To the south is an exit to a small room.", 
[], 
"UBC")

utp_hallway = Room("UTP Hallway", 
["UTP Lounge", "UTP Classroom Hallway", "none", "UTP Balcony", "Chalkboard"],
None, 
"You are in a small hallway. To the north is a door to a small room, and to the south is another hallway. To the west is an exit. There are chalkboards here.", 
["Box Robot", "Student"], 
"UBC")

utp_far_eli = Room("UTP Far ELI", 
["none", "none", "none", "UTP Balcony"], 
None,
"You are in a large room with robots strewn on tables. There is a closed box here. To the west is a balcony.", 
["Bagle"], 
"UBC",
"💌")

utp_balcony = Room("UTP Balcony", 
["UTP Lockers", "UTP Far ELI",  "UTP Hallway", "UTP Driveway", "UTP Middle ELI", "UTP North ELI"],
None,
"You are on a long balcony outside. To the west is a staircase to the driveway. To the north is a room with lockers, to the east is a hallway, and to the south is an ELI room.", 
["Box Robot", "Student"], 
"UBC")

utp_driveway = Room("UTP Driveway", 
["Downstairs Classroom", "UTP Alcove", "UTP Balcony", "West Mall"], 
None,
"You are in a snowy driveway leading to an old wooden building. To the east is a staircase leading to a long balcony. To the west is West Mall.", 
["Box Robot", "Student"], 
"UBC")

chalkboard = Room("Chalkboard",
["none", "none", "none", "none", "Canada Place", "u37"],
None,
"You went inside the chalkboard and realized it was a teleporter. You saw two exits, one marked \"Canada Place\", and the other marked \"u37\". Before you knew what was happening, one of the portals swallowed you up.",
[],
"UBC")

utp_north_eli = Room("UTP North ELI",
["none", "none", "none", "UTP Balcony"],
None,
"You are in the north ELI room at UTP. There is nothing here right now. To the west is a balcony.",
["Box Robot", "Student"],
"UBC")

utp_middle_eli = Room("UTP Middle ELI",
["none", "none", "none", "UTP Balcony"],
"Try `>print <item>` for some <item>.",
"You are in the middle ELI room at UTP. To the west is a balcony.\n\nThere is a 3D printer here.",
["Box Robot", "Student"],
"UBC")

utp_classroom_hallway = Room("UTP Classroom Hallway",
["UTP Hallway", "UTP English Classroom", "UTP History Classroom", "UTP Balcony", "UTP Science Classroom"],
None,
"You are in a hallway lined with classrooms. To the north is another hallway, and to the west is an exit. There are classrooms to the east and south.",
["Box Robot", "Student"],
"UBC")

utp_english_classroom = Room("UTP English Classroom",
["UTP Classroom Hallway", "none", "none", "none"],
None,
"You are in a classroom. There is nothing here right now. To the north is a hallway.",
["Box Robot", "Student"],
"UBC")

utp_history_classroom = Room("UTP History Classroom",
["none", "none", "none", "UTP Classroom Hallway"],
None,
"You are in a classroom. There is nothing here right now. To the west is a hallway.",
["Box Robot", "Student"],
"UBC")

utp_science_classroom = Room("UTP Science Classroom",
["none", "none", "none", "UTP Classroom Hallway"],
None,
"You are in a classroom. There is nothing here right now. To the west is a hallway.",
["Box Robot", "Student"],
"UBC")

downstairs_classroom = Room("Downstairs Classroom",
["none", "UTP Driveway", "none", "none"],
None,
"You are in a small classroom underneath UTP. There is nothing here right now. To the south is a driveway.",
["Box Robot", "Student"],
"UBC")

alcove = Room("UTP Alcove",
["UTP Driveway", "none", "none", "none"],
None,
"You are in a small space underneath UTP. There is nothing here right now. To the north is a driveway.",
["Box Robot", "Student"],
"UBC")