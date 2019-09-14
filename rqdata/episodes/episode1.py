npclist = ["Box Robot", "Student", "Seagull", "Pigeon", "Crow", "Cookie", "Diwheel"]

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
["UTP Lockers", "UTP Office", "UTP Hallway"], 
["UTP Office", "UTP Hallway", "none", "UTP Lockers"], 
"You are standing in a small room with some tables in the middle. A fridge is sitting to one side, and a small hallway goes out the other. There is a tiny office behind you alongside some lockers.", 
[], 
"UBC")

utp_lockers = Room("UTP Lockers", 
["UTP Lounge", "UTP Balcony"], 
["none", "none", "UTP Lounge", "UTP Balcony"], 
"You are in front of a wall of lockers. They are all locked. There is one with your name on it which you happen to know the password to.", 
[], 
"UBC")

utp_office = Room("UTP Office", 
["UTP Lounge"], 
["none", "none", "UTP Lounge", "none"], 
"You are in a tiny office outside the small room. There are numerous computers stored to one side. One of them has a virtual fishing game running.", 
[], 
"UBC")

utp_hallway = Room("UTP Hallway", 
["UTP Lounge", "UTP Balcony", "Chalkboard"], 
["UTP Lounge", "none", "none", "UTP Balcony"], 
"You are in a small hallway to the side of the room. There are chalkboards on the walls, and a doorway leading to a balcony.", 
["Box Robot", "Student"], 
"UBC")

utp_eli = Room("UTP ELI", 
["UTP Balcony"], 
["none", "none", "none", "UTP Balcony"], 
"You are in a large room with robots strewn on tables. There is a closed box here.", 
["Bagle"], 
"UBC",
"💌")

utp_balcony = Room("UTP Balcony", 
["UTP Hallway", "UTP Lockers", "UTP Driveway", "UTP ELI"], 
["UTP Lockers", "UTP ELI",  "UTP Hallway", "UTP Driveway"], 
"You are on a long balcony outside. Behind you is a staircase to the driveway, and to your sides and front are three doorways.", 
["Box Robot", "Student"], 
"UBC")

utp_driveway = Room("UTP Driveway", 
["UTP Balcony", "West Mall"], 
["none", "none", "UTP Balcony", "West Mall"], 
"You are in a snowy driveway leading to an old wooden building. There is a staircase leading to a long balcony. To the west is West Mall.", 
["Box Robot", "Student"], 
"UBC")

agricultural_road_west = Room("Agricultural Road West", 
["Agricultural at West", "Agricultural at Main"], 
["none", "none", "Agricultural at Main", "Agricultural at West"], 
"You are on the west half of a vast east-west road. To the east is Main Mall and to the west is West Mall.", 
["Student"], 
"UBC")

agricultural_road_east = Room("Agricultural Road East",
["Agricultural at Main", "Agricultural at East", "IKB Library"],
["IKB Library", "none", "Agricultural at East", "Agricultural at Main"], 
"You are on the east half of vast east-west road. To the west is Main Mall, and to the east is East Mall. To the north is a library.", 
["Student"], 
"UBC")

agricultural_at_main = Room("Agricultural at Main", 
["Main Mall Centre North", "Main Mall North", "Agricultural Road West", "Agricultural Road East"], 
["Main Mall North", "Main Mall Centre North", "Agricultural Road East", "Agricultural Road West"], 
"You are at the intersection of Agricultural Road and Main Mall.", 
["Student", "Diwheel"], 
"UBC")

main_mall_centre_north = Room("Main Mall Centre North", 
["University at Main", "Agricultural at Main"], 
["Agricultural at Main", "University at Main", "none", "none"], 
"You are on the north central section of a vast north-south road. To the north is Agricultural Road, and to the south is University Boulevard. ", 
["Student", "Diwheel"], 
"UBC")

university_at_main = Room("University at Main", 
["Main Mall Centre North", "Main Mall Centre South", "Martha Piper Fountain", "University Boulevard West"], 
["Main Mall Centre North", "Main Mall Centre South", "University Boulevard West", "none"], 
"You are at the intersection of University Boulevard and Main Mall. There is a fountain here, but it its frozen over.", 
["Student", "Diwheel"], 
"UBC")

main_mall_centre_south = Room("Main Mall Centre South", 
["University at Main", "The Cairn"], 
["University at Main", "The Cairn", "none", "none"], 
"You are on the north section of a vast north-south road. To the north is University Boulevard, and to the south is a cairn with Es visible on it. Christmas lights are strung on lampposts here.", 
["Student", "Diwheel"], 
"UBC")

agricultural_at_east = Room("Agricultural at East",
["East Mall", "Agricultural Road East", "Nest Walkway"], 
["none", "East Mall", "Nest Walkway", "Agricultural Road East"], 
"You are at the intersection of Agricultural Road and East Mall.", 
["Student"], 
"UBC")

main_mall_north = Room("Main Mall North", 
["Agricultural at Main", "Rose Garden", "IKB Library"], 
["Rose Garden", "Agricultural at Main", "IKB Library", "none"], 
"You are on the north section of a vast north-south road. To the north is a rose garden, and to the south is Agricultural Road. To the east is a library.", 
["Student", "Diwheel"], 
"UBC")

nest_walkway = Room("Nest Walkway", 
["none", "The Nest", "UBC Bus Loop", "Agricultural at East"],
None, 
"You are on a thin west-east walkway. To the west is East Mall, and to the east is a looping road with buses. There is a building to the south.", 
["Student"], 
"UBC")

martha_piper_fountain = Room("Martha Piper Fountain", 
["University at Main"], 
["University at Main", "University at Main", "University at Main", "University at Main"], 
"You are at a circular fountain. There is water here, but it is underneath a thick layer of solid ice and snow. There is a closed box here.", 
["Diwheel Transformer"], 
"UBC",
"🛡")

the_cairn = Room("The Cairn", 
["Main Mall Centre South"], 
["Main Mall Centre South", "none", "none", "none"], 
"You are at a cairn with a red E inscribed on 3 sides. A long road leads north. There is a box here.", 
["Flying Doge"], 
"UBC",
"🍰")

rose_garden = Room("Rose Garden", 
["Main Mall North"], 
["none", "Main Mall North", "none", "none"], 
"You are at a vast garden with numerous flowers. A long road leads south. There is a box here.", 
["Lovesick Student"], 
"UBC",
"🚩")

the_nest = Room("The Nest", 
["East Mall", "Nest Walkway"], 
["Nest Walkway", "none", "none", "East Mall"], 
"You are in a large building with many floors. There are shops here but you have no money. There are exits to the west and north here. On a nearby table, there is a closed box.", 
["Hungry Student"], 
"UBC",
"💌")

east_mall = Room("East Mall", 
["The Nest", "Agricultural at East", "University at East"], 
["Agricultural at East", "University at East", "The Nest","none"], 
"You are on a thin north-south road. To the south is University Boulevard, and to the north is Agricultural Road. To the east is a large building with shops in it.", 
["Student"], 
"UBC")

ubc_bookstore = Room("UBC Bookstore", 
["University at East"], 
["University at East", "none", "none", "none"], 
"You are in an underground bookstore. To the north is University Boulevard. There is a sign here that says:\n\n**📣 and 🔦 for sale.** \n*for your late night exam commutes*\n*50 coins per item\nAvailable for 5000 coins:📇", 
[], 
"UBC")

ubc_bus_loop = Room("UBC Bus Loop", 
["none", "University at Wesbrook", "none", "Nest Walkway"], 
None,
"You are at a looping road at the east end of the east-west road. To the south is University Boulevard and to the west is a thin walkway. \nThere are bus stops here for:\n\n25\n43\n44\n68\n84\n99\n480", 
[], 
"UBC")

yubot_bank_ubc = Room("YuBot Bank UBC", 
["University at Wesbrook"], 
["University at Wesbrook", "none", "none", "none"], 
"You are at the UBC branch of the YuBot bank. To the north is University Boulevard.", 
[], 
"UBC")

university_boulevard_west = Room("University Boulevard West", ["University at Main", "University at East"], 
["none", "none", "University at East", "University at Main"], 
"You are on the west section of an east-west road with a frozen waterfall. To the west is Main Mall, and to the east is East Mall.", 
["Student"], 
"UBC")

university_at_east = Room("University at East", 
["UBC Bookstore", "University Boulevard West", "East Mall", "University Boulevard East"], 
["East Mall", "UBC Bookstore", "University Boulevard East", "University Boulevard West"], 
"You are at the intersection of University Boulevard and East Mall. To the south is a bookstore.", 
["Student"], 
"UBC")

ikb_library = Room("IKB Library", 
["Main Mall North", "Agricultural Road East"], 
["none", "Agricultural Road East", "none", "Main Mall North"], 
"You are in an enormous library. There are books here. There are exits to the west and south here.", 
[], 
"UBC")

university_boulevard_east = Room("University Boulevard East", ["University at East", "University at Wesbrook"], 
["none", "none", "University at Wesbrook", "University at East"], 
"You are on the east section of an east-west road. To the west is East Mall, and to the east is Wesbrook Mall.", 
["Student"], 
"UBC")

university_at_wesbrook = Room("University at Wesbrook", ["YuBot Bank UBC", "UBC Bus Loop", "University Boulevard East", "Pacific Spirit Maze​"], 
["UBC Bus Loop", "YuBot Bank UBC", "Pacific Spirit Maze​", "University Boulevard East"], 
"You are at the intersection of University Boulevard and Wesbrook Mall. To the north is a looping road with buses and to the south is a small bank. To the east is a mysterious maze guarded by walls of dense trees.", 
["Student"], 
"UBC")

pacific_spirit_maze0 = Room("Pacific Spirit Maze​",["University at Wesbrook", "Pacific Spirit Maze ​", "Pacific Spirit Maze  ​", "Pacific Spirit Maze   ​"], 
["Pacific Spirit Maze ​", "Pacific Spirit Maze   ​", "Pacific Spirit Maze  ​", "University at Wesbrook"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze1 = Room("Pacific Spirit Maze ​",
["Pacific Spirit Maze​", "Pacific Spirit Maze    ​", "Pacific Spirit Maze        ​"],
["Pacific Spirit Maze    ​", "Pacific Spirit Maze​", "Pacific Spirit Maze        ​", "none"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze2 = Room("Pacific Spirit Maze  ​",
["Pacific Spirit Maze​", "Pacific Spirit Maze          ​", "Pacific Spirit Maze           ​"], 
["Pacific Spirit Maze          ​", "Pacific Spirit Maze           ​", "none", "Pacific Spirit Maze​"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze3 = Room("Pacific Spirit Maze   ​",["Pacific Spirit Maze​", "Pacific Spirit Maze            ​"], ["Pacific Spirit Maze​", "none", "Pacific Spirit Maze            ​", "none"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze4 = Room("Pacific Spirit Maze    ​",["Pacific Spirit Maze ​", "Pacific Spirit Maze     ​"], 
["none", "Pacific Spirit Maze ​", "Pacific Spirit Maze     ​", "none"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze5 = Room("Pacific Spirit Maze     ​",["Pacific Spirit Maze    ​", "Pacific Spirit Maze      ​"],
["none", "Pacific Spirit Maze      ​", "none", "Pacific Spirit Maze    ​"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze6 = Room("Pacific Spirit Maze      ​",["Pacific Spirit Maze     ​", "Pacific Spirit Maze       ​", "Pacific Spirit Maze        ​"], 
["Pacific Spirit Maze     ​", "Pacific Spirit Maze       ​","none", "Pacific Spirit Maze        ​"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze7 = Room("Pacific Spirit Maze       ​",["Pacific Spirit Maze      ​"], 
["Pacific Spirit Maze      ​", "none", "none", "none"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze8 = Room("Pacific Spirit Maze        ​",["Pacific Spirit Maze ​", "Pacific Spirit Maze      ​", "Pacific Spirit Maze         ​"], 
["none", "Pacific Spirit Maze         ​", "Pacific Spirit Maze      ​", "Pacific Spirit Maze ​"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze9 = Room("Pacific Spirit Maze         ​",["Pacific Spirit Maze        ​", "Pacific Spirit Maze          ​"], 
["Pacific Spirit Maze        ​", "none", "none", "Pacific Spirit Maze          ​"],
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same. There is a closed box here.", 
["Treasure Hunter Student"], 
"UBC",
"🕯")

pacific_spirit_maze10 = Room("Pacific Spirit Maze          ​",["Pacific Spirit Maze  ​", "Pacific Spirit Maze         ​"], 
["none", "Pacific Spirit Maze  ​", "Pacific Spirit Maze         ​", "none"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze11 = Room("Pacific Spirit Maze           ​",["Pacific Spirit Maze  ​", "Pacific Spirit Maze            ​"],
["Pacific Spirit Maze  ​", "none", "none", "Pacific Spirit Maze            ​"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

pacific_spirit_maze12 = Room("Pacific Spirit Maze            ​",
["Pacific Spirit Maze   ​", "Pacific Spirit Maze           ​"], 
["none", "none", "Pacific Spirit Maze           ​", "Pacific Spirit Maze   ​"], 
"You are in a twisty, winding maze with walls of dense trees. Everything looks the same.", 
["Student"], 
"UBC")

memorial_at_west = Room("Memorial at West", 
["West Mall"], 
["none", "West Mall", "none", "none"], 
"You are at the intersection of Memorial Road and West Mall. There is a bus stop here for\n\n68", 
[], 
"UBC")

west_mall = Room("West Mall", 
["Memorial at West", "UTP Driveway", "Agricultural at West"], 
["Memorial at West", "Agricultural at West", "UTP Driveway", "none"], 
"You are on a short north-south roadway. To the north is Memorial Road and to the south is Agricultural Road. To the east is a small snowy driveway to an old wooden building.", 
["Student"], 
"UBC")

agricultural_at_west = Room("Agricultural at West", 
["Agricultural Road West", "West Mall"], 
["West Mall", "none", "Agricultural Road West", "none"], 
"You are at the intersection of Agricultural Road and West Mall.", 
["Student"], 
"UBC")

sixty_eight = Room("68", 
["Memorial at West", "UBC Bus Loop"], 
["none", "none", "none", "none"], 
"You are in a bus running route 68. You can go to the following destinations:\n\n"+"\n".join(["Memorial at West", "UBC Bus Loop"]), 
[], 
"UBC")

chalkboard = Room("Chalkboard",
["Canada Place", "UTP Hallway"],
["UTP Hallway", "none", "none", "none"],
"You went inside the chalkboard and realized it was a teleporter. You can see portals leading to the following locations here:\n\nCanada Place\n\nTo the north is the way back into the hallway.",
[],
"UBC")

#-----------------------end of UBC rooms---------------------

forty_four = Room("44",
["UBC Bus Loop", "Waterfront Station"],
["none", "none", "none", "none"], 
"You are in a bus running route 44. You can go to the following destinations:\n\n"+"\n".join(["UBC Bus Loop", "Waterfront Station"]), 
[], 
"Downtown Vancouver")

waterfront_station = Room("Waterfront Station", 
["600 Block West Cordova Street"],
["none", "600 Block West Cordova Street", "none", "none"],
"You are in an old, busy transit terminal. To the south is Cordova Street. There is a Canada Line station here.\nThere is a bus stop here for:\n\n10\n44",
[],
"Downtown Vancouver")

west_cordova_600_block = Room("600 Block West Cordova Street",
["Waterfront Station", "Cordova at Granville"],
["Waterfront Station", "none", "none", "Cordova at Granville"],
"You are at the 600 block of a short east-west road. To the north is an old transit terminal and to the west is Granville Street.",
["Seagull"],
"Downtown Vancouver")

cordova_at_granville = Room("Cordova at Granville",
["600 Block West Cordova Street", "700 Block West Cordova Street", "300 Block Granville Street"],
["none", "300 Block Granville Street", "600 Block West Cordova Street", "700 Block West Cordova Street"],
"You are at the intersection of Cordova Street and Granville Street.",
["Seagull"],
"Downtown Vancouver")

west_cordova_700_block = Room("700 Block West Cordova Street",
["Cordova at Granville", "Cordova at Howe"],
["none", "none", "Cordova at Granville", "Cordova at Howe"],
"You are at the 700 block of a short east-west road. To the east is Granville Street and to the west is Howe Street.",
["Seagull"],
"Downtown Vancouver")

cordova_at_howe = Room("Cordova at Howe",
["700 Block West Cordova Street", "800 Block West Cordova Street", "200 Block Howe Street"],
["200 Block Howe Street", "none", "700 Block West Cordova Street", "800 Block West Cordova Street"],
"You are at the intersection of Cordova Street and Howe Street.",
["Seagull"],
"Downtown Vancouver")

west_cordova_800_block = Room("800 Block West Cordova Street",
["Cordova at Howe", "Cordova at Burrard"],
["none", "none", "Cordova at Howe", "Cordova at Burrard"],
"You are at the 800 block of a short east-west road. To the east is Howe Street and to the west is Burrard Street.",
["Seagull"],
"Downtown Vancouver")

cordova_at_burrard = Room("Cordova at Burrard",
["800 Block West Cordova Street", "1000 Block West Cordova Street", "200 Block Burrard Street"],
["200 Block Burrard Street", "none", "800 Block West Cordova Street", "1000 Block West Cordova Street"],
"You are at the intersection of Cordova Street and Burrard Street.",
["Seagull","Cookie"],
"Downtown Vancouver")

west_cordova_1000_block = Room("1000 Block West Cordova Street",
["Cordova at Burrard", "Cordova at Thurlow"],
["none", "none", "Cordova at Burrard", "Cordova at Thurlow"],
"You are at the 1000 block of a short east-west road. To the east is Burrard Street and to the west is Thurlow Street.",
["Seagull"],
"Downtown Vancouver")

cordova_at_thurlow = Room("Cordova at Thurlow",
["1000 Block West Cordova Street", "200 Block Thurlow Street"],
["200 Block Thurlow Street", "none", "1000 Block West Cordova Street", "none"],
"You are at the intersection of Cordova Street and Thurlow Street.",
["Seagull"],
"Downtown Vancouver")

howe_200_block = Room("200 Block Howe Street",
["Cordova at Howe", "Canada Place at Howe"],
["Canada Place at Howe", "Cordova at Howe", "none", "none"],
"You are at the 200 block of a north-south road. To the south is Cordova Street and to the north is Canada Place.",
["Seagull"],
"Downtown Vancouver")

burrard_200_block = Room("200 Block Burrard Street",
["Cordova at Burrard", "Canada Place at Burrard"],
["Canada Place at Burrard", "Cordova at Burrard", "none", "none"],
"You are at the 200 block of a north-south road. To the south is Cordova Street and to the north is Canada Place.",
["Seagull", "Cookie"],
"Downtown Vancouver")

thurlow_200_block = Room("200 Block Thurlow Street",
["Cordova at Thurlow", "Canada Place at Burrard"],
["Canada Place at Thurlow", "Cordova at Thurlow", "none", "none"],
"You are at the 200 block of a north-south road. To the south is Cordova Street and to the north is Canada Place.",
["Seagull"],
"Downtown Vancouver")

canada_place_800_block = Room("800 Block Canada Place",
["Canada Place at Howe", "Canada Place at Burrard"],
["none", "none", "Canada Place at Howe", "Canada Place at Burrard"],
"You are at the 800 block of an east-west road. To the east is Howe Street and to the west is Burrard Street.",
["Seagull"],
"Downtown Vancouver")

canada_place_1000_block = Room("1000 Block Canada Place",
["Canada Place at Thurlow", "Canada Place at Burrard", "Vancouver Convention Centre"],
["Vancouver Convention Centre", "none", "Canada Place at Burrard", "Canada Place at Thurlow"],
"You are at the 1000 block of an east-west road. To the east is Burrard Street and to the west is Thurlow Street. To the north is a large convention centre.",
["Seagull"],
"Downtown Vancouver")

canada_place_at_howe = Room("Canada Place at Howe",
["800 Block Canada Place", "200 Block Howe Street"],
["none", "200 Block Howe Street", "none", "800 Block Canada Place"],
"You are at the intersection of Canada Place and Howe Street.",
["Seagull"],
"Downtown Vancouver")

canada_place_at_burrard = Room("Canada Place at Burrard",
["800 Block Canada Place", "200 Block Burrard Street", "1000 Block Canada Place"],
["none", "200 Block Burrard Street", "800 Block Canada Place", "1000 Block Canada Place"],
"You are at the intersection of Canada Place and Burrard Street.",
["Seagull", "Cookie"],
"Downtown Vancouver")

canada_place_at_thurlow = Room("Canada Place at Thurlow",
["1000 Block Canada Place", "200 Block Thurlow Street"],
["none", "200 Block Thurlow Street", "1000 Block Canada Place", "none"],
"You are at the intersection of Canada Place and Thurlow Street.",
["Seagull"],
"Downtown Vancouver")

vancouver_convention_centre = Room("Vancouver Convention Centre",
["1000 Block Canada Place"],
["none", "1000 Block Canada Place", "none", "none"],
"You are in a large convention centre. To the south is Canada Place. There is a box here.",
["Obsessed Comic Fan"],
"Downtown Vancouver",
"📰")

canada_place = Room("Canada Place",
["800 Block Canada Place"],
["none", "800 Block Canada Place", "none", "none"],
"You are in a building on the east side of Canada Place. There is nothing here right now. To the south is Canada Place.",
[],
"Downtown Vancouver")

granville_300_block = Room("300 Block Granville Street",
["Cordova at Granville", "YuBot Bank Downtown Vancouver", "Hastings at Granville"],
["Cordova at Granville", "Hastings at Granville", "YuBot Bank Downtown Vancouver", "none"],
"You are at the 300 block of a long north south road. To the north is Cordova Street and to the south is Hastings Street. To the east is a bank.",
["Seagull"],
"Downtown Vancouver")

yubot_bank_downtown_vancouver = Room("YuBot Bank Downtown Vancouver", 
["300 Block Granville Street"], 
["none", "none", "none", "300 Block Granville Street"], 
"You are at the Downtown Vancouver branch of the YuBot bank. To the west is Granville Street.", 
[], 
"Downtown Vancouver")

hastings_at_granville = Room("Hastings at Granville",
["300 Block Granville Street", "400 Block Granville Street"],
["300 Block Granville Street", "400 Block Granville Street", "none", "none"],
"You are at the intersection of Hastings Street and Granville Street. There is a bus stop here for\n10",
[],
"Downtown Vancouver")

granville_400_block = Room("400 Block Granville Street",
["Pender at Granville", "Hastings at Granville"],
["Hastings at Granville", "Pender at Granville", "none", "none"],
"You are at the 400 block of a long north south road. To the north is Hastings Street and to the south is Pender Street.",
["Seagull"],
"Downtown Vancouver")

pender_at_granville = Room("Pender at Granville",
["400 Block Granville Street", "500 Block Granville Street"],
["400 Block Granville Street", "500 Block Granville Street", "none", "none"],
"You are at the intersection of Pender Street and Granville Street. There is a bus stop here for\n\n19",
[],
"Downtown Vancouver")

granville_500_block = Room("500 Block Granville Street",
["Pender at Granville", "Dunsmuir at Granville"],
["Pender at Granville", "Dunsmuir at Granville", "none", "none"],
"You are at the 500 block of a long north south road. To the north is Pender Street and to the south is Dunsmuir Street.",
["Seagull"],
"Downtown Vancouver")

dunsmuir_at_granville = Room("Dunsmuir at Granville",
["500 Block Granville Street", "600 Block Granville Street"],
["500 Block Granville Street", "600 Block Granville Street", "none", "none"],
"You are at the intersection of Dunsmuir Street and Granville Street.",
["Seagull"],
"Downtown Vancouver")

granville_600_block = Room("600 Block Granville Street",
["Dunsmuir at Granville", "Georgia at Granville"],
["Dunsmuir at Granville", "Georgia at Granville", "none", "none"],
"You are at the 600 block of a long north south road. To the north is Dunsmuir Street and to the south is Georgia Street.",
["Seagull"],
"Downtown Vancouver")

georgia_at_granville = Room("Georgia at Granville",
["600 Block Granville Street", "700 Block Granville Street", "none", "Vancouver City Centre Station"],
None,
"You are at the intersection of Georgia Street and Granville Street. To the west is a Canada Line station. There is a bus stop here for \n\n250",
[],
"Downtown Vancouver")

vancouver_city_centre_station = Room("Vancouver City Centre Station",
["none", "none", "Georgia at Granville", "none"],
None,
"You are in the Vancouver City Centre Canada Line station. To the east is Granville Street.",
[],
"Downtown Vancouver")

granville_700_block = Room("700 Block Granville Street",
["Georgia at Granville", "Robson at Granville"],
["Georgia at Granville", "Robson at Granville", "none", "none"],
"You are at the 700 block of a long north south road. To the north is Georgia Street and to the south is Robson Street.",
["Seagull"],
"Downtown Vancouver")

robson_at_granville = Room("Robson at Granville",
["700 Block Granville Street", "700 Block Robson Street", "600 Block Robson Street"],
["700 Block Granville Street", "none", "600 Block Robson Street", "700 Block Robson Street"],
"You are at the intersection of Robson Street and Granville Street. There is a bus stop here for\n10",
[],
"Downtown Vancouver")

robson_700_block = Room("700 Block Robson Street",
["Robson at Granville", "Robson at Howe"],
["none", "none", "Robson at Granville", "Robson at Howe"],
"You are at the 700 block of an east-west road. To the east is Granville Street and to the west is Howe Street.",
["Seagull"],
"Downtown Vancouver")

robson_at_howe = Room("Robson at Howe",
["700 Block Robson Street", "Robson Square"],
["none", "none", "700 Block Robson Street", "Robson Square"],
"You are at the intersection of Robson and Howe. To the west is Robson Square.",
["Seagull"],
"Downtown Vancouver")

robson_square = Room("Robson Square",
["none", "none", "Robson at Howe", "none", "Robson Square Ice Rink"],
None,
"You are on an expansive outdoor square with tables everywhere. There is a food cart here with free samples in a fridge. To the east is Howe Street. Nearby are entrances to what appears to be an ice rink.",
[],
"Downtown Vancouver")

robson_square_ice_rink = Room("Robson Square Ice Rink",
["Robson Square"],
["Robson Square", "Robson Square", "Robson Square", "Robson Square"],
"You are in a skating rink underneath robson square. There is a box here.",
["Skater"],
"Downtown Vancouver",
"❄")

robson_600_block = Room("600 Block Robson Street",
["Robson at Granville", "Robson at Seymour"],
["none", "none", "Robson at Seymour", "Robson at Granville"],
"You are at the 600 block of an east-west road. To the east is Seymour Street and to the west is Granville Street.",
["Seagull"],
"Downtown Vancouver")

robson_at_seymour = Room("Robson at Seymour",
["600 Block Robson Street", "500 Block Robson Street"],
["none", "none", "500 Block Robson Street", "600 Block Robson Street"],
"You are at the intersection of Robson and Seymour.",
["Seagull"],
"Downtown Vancouver")

robson_500_block = Room("500 Block Robson Street",
["Robson at Richards", "Robson at Seymour", "YuBot Gift Shop Downtown Vancouver"],
["none", "YuBot Gift Shop Downtown Vancouver", "Robson at Richards", "Robson at Seymour"],
"You are at the 500 block of an east-west road. To the east is Richards Street and to the west is Seymour Street. To the south is a gift shop.",
["Seagull"],
"Downtown Vancouver")

robson_at_richards = Room("Robson at Richards",
["400 Block Robson Street", "500 Block Robson Street"],
["none", "none", "400 Block Robson Street", "500 Block Robson Street"],
"You are at the intersection of Robson and Richards.",
["Seagull"],
"Downtown Vancouver")

robson_400_block = Room("400 Block Robson Street",
["Robson at Richards", "Robson at Homer"],
["none", "none", "Robson at Homer", "Robson at Richards"],
"You are at the 400 block of an east-west road. To the east is Homer Street and to the west is Richards Street.",
["Seagull"],
"Downtown Vancouver")

robson_at_homer = Room("Robson at Homer",
["400 Block Robson Street", "700 Block Homer Street"],
["700 Block Homer Street", "none", "none", "400 Block Robson Street"],
"You are at the intersection of Robson and Homer.",
["Seagull"],
"Downtown Vancouver")

homer_700_block = Room("700 Block Homer Street",
["Robson at Homer", "Georgia at Homer", "Vancouver Public Library Central Branch"],
["Georgia at Homer", "Robson at Homer", "Vancouver Public Library Central Branch", "none"],
"You are on a short north-south road. To the north is Georgia Street and to the south is Robson Street. To the east is a large library.",
["Seagull"],
"Downtown Vancouver")

georgia_at_homer = Room("Georgia at Homer",
["700 Block Homer Street"],
["none", "700 Block Homer Street", "none", "none"],
"You are at the intersection of Georgia and Homer. There is a bus stop here for \n\n250",
[],
"Downtown Vancouver")

vancouver_public_library_central_branch = Room("Vancouver Public Library Central Branch", 
["700 Block Homer Street"], 
["none", "none", "none", "700 Block Homer Street"], 
"You are in an enormous library. There are books here. There is an exit to the west here.", 
[], 
"Downtown Vancouver")

two_fifty = Room("250",
["Georgia at Homer", "Georgia at Granville"],
["none", "none", "none", "none"], 
"You are in a bus running route 250. You can go to the following destinations:\n\n"+"\n".join(["Georgia at Homer", "Georgia at Granville"]), 
[], 
"Downtown Vancouver")

ten = Room("10",
["Waterfront Station", "Hastings at Granville", "Robson at Granville", "5th at Granville", "41st at Granville", "Marine at Cambie"],
["none", "none", "none", "none"], 
"You are in a bus running route 10. You can go to the following destinations:\n\n"+"\n".join(["Waterfront Station", "Hastings at Granville", "Robson at Granville", "5th at Granville", "41st at Granville", "Marine at Cambie"]), 
[], 
"Downtown Vancouver")

yubot_gift_shop_downtown_vancouver = Room("YuBot Gift Shop Downtown Vancouver", 
["500 Block Robson Street"], 
["500 Block Robson Street", "none", "none", "none"], 
"You are in a small gift shop. To the north is Robson Street. There is a sign here that says:\n\nAvailable for 50 coins:📣\nAvailable for 50 coins:🔦\nAvailable for 5000 coins:📇", 
[], 
"Downtown Vancouver")

#------- ------End of Downtown Vancouver Rooms---------------

fifth_at_granville = Room("5th at Granville",
["2000 Block Granville Street"],
["2000 Block Granville Street", "none", "none", "none"],
"You are at the intersection of 5th Avenue and Granville Street. There is a bus stop here for \n\n10",
[],
"Granville Island")

granville_2000_block = Room("2000 Block Granville Street",
["5th at Granville", "4th at Anderson"],
["4th at Anderson", "5th at Granville", "none", "none"],
"You are at the 2000 block of a long north-south road. To the north is 4th Avenue and to the south is 5th Avenue.",
["Seagull"],
"Granville Island")

fourth_at_anderson = Room("4th at Anderson",
["2000 Block Granville Street", "1900 Block Anderson Street", "1500 Block 4th Avenue"],
["1900 Block Anderson Street", "2000 Block Granville Street", "none", "1500 Block 4th Avenue"],
"You are at the intersection of 4th Avenue and Anderson Street.",
["Seagull"],
"Granville Island")

fourth_1500_block = Room("1500 Block 4th Avenue",
["4th at Fir", "4th at Anderson"],
["none", "none", "4th at Anderson", "4th at Fir"],
"You are at the 1500 block of a short east-west road. To the east is Anderson Street and to the west is Fir Street.",
["Seagull"],
"Granville Island")

fourth_at_fir = Room("4th at Fir",
["1500 Block 4th Avenue"],
["none", "none", "1500 Block 4th Avenue", "none"],
"You are at the intersection of 4th Avenue and Fir Street. There is a bus stop here for \n\n84",
[],
"Granville Island")

eighty_four = Room("84",
["UBC Bus Loop", "4th at Fir", "500 Block 2nd Avenue"],
["none", "none", "none", "none"],
"You are in a bus running route 84. You can go to the following destinations:\n\n"+"\n".join(["UBC Bus Loop", "4th at Fir", "500 Block 2nd Avenue"]),
[],
"Granville Island")

anderson_1900_block = Room("1900 Block Anderson Street",
["4th at Anderson", "3rd at Anderson"],
["3rd at Anderson", "4th at Anderson", "none", "none"],
"You are at the 1900 block of a north-south road. To the north is 3rd Avenue and to the south is 4th Avenue.",
["Seagull"],
"Granville Island")

third_at_anderson = Room("3rd at Anderson",
["1800 Block Anderson Street", "1900 Block Anderson Street"],
["1800 Block Anderson Street", "1900 Block Anderson Street", "none", "none"],
"You are at the intersection of 3rd Avenue and Anderson Street.",
["Seagull"],
"Granville Island")

anderson_1800_block = Room("1800 Block Anderson Street",
["Lamey's Mill at Anderson", "3rd at Anderson"],
["Lamey's Mill at Anderson", "3rd at Anderson", "none", "none"],
"You are at the 1800 block of a north-south road. To the north is Lamey's Mill Road and to the south is 3rd Avenue.",
["Seagull"],
"Granville Island")

lameys_mill_at_anderson = Room("Lamey's Mill at Anderson",
["Granville Island Entrance", "1800 Block Anderson Street"],
["Granville Island Entrance", "1800 Block Anderson Street", "none", "none"],
"You are at the intersection of Lamey's Mill Road and Anderson Street. There is a bus stop here for\n\n50",
[],
"Granville Island")

granville_island_entrance = Room("Granville Island Entrance",
["Cartwright at Anderson", "Lamey's Mill at Anderson"],
["Cartwright at Anderson", "Lamey's Mill at Anderson", "none", "none"],
"You are at the entrance to Granville Island. To the north is Cartwright Street and to the south is Lamey's Mill Road.",
["Seagull"],
"Granville Island")

cartwright_at_anderson = Room("Cartwright at Anderson", 
["Anderson Street Granville Island", "Granville Island Entrance", "Cartwright Street West", "Duranleau Street"],
["Anderson Street Granville Island", "Granville Island Entrance", "Cartwright Street West", "Duranleau Street"],
"You are at the intersection of Cartwright Street and Anderson Street.",
["Seagull"],
"Granville Island")

anderson_street_granville_island = Room("Anderson Street Granville Island",
["Johnston at Anderson", "Cartwright at Anderson"],
["Johnston at Anderson", "Cartwright at Anderson", "none", "none"],
"You are on Anderson Street in Granville Island. To the north is Johnston Street and to the south is Cartwright Street.",
["Seagull"],
"Granville Island")

cartwright_street_west = Room("Cartwright Street West",
["Cartwright at Old Bridge", "Cartwright at Anderson", "YuBot Gift Shop Granville Island"],
["none", "YuBot Gift Shop Granville Island", "Cartwright at Old Bridge", "Cartwright at Anderson"],
"You are on a small east-west road. To the east is Old Bridge Street and to the west is Anderson Street. To the south is a gift shop.",
["Seagull"],
"Granville Island")

cartwright_at_old_bridge = Room("Cartwright at Old Bridge",
["Cartwright Street East", "Cartwright Street West"],
["none", "none", "Cartwright Street East", "Cartwright Street West"],
"You are at the intersection of Cartwright Street and Old Bridge Street.",
["Seagull"],
"Granville Island")

cartwright_street_east = Room("Cartwright Street East",
["Cartwright at Old Bridge", "Cartwright at Johnston"],
["Cartwright at Johnston", "none", "none", "Cartwright at Old Bridge"],
"You are on a small winding road. To the north is Johnston Street and to the west is Old Bridge Street.",
["Seagull"],
"Granville Island")

cartwright_at_johnston = Room("Cartwright at Johnston",
["Cartwright Street East", "Johnston Street East"],
["none", "Cartwright Street East", "none", "Johnston Street East"],
"You are at the intersection of Cartwright Street and Johnston Street.",
["Seagull"],
"Granville Island")

johnston_street_east = Room("Johnston Street East", 
["Cartwright at Johnston", "Johnston at Old Bridge"],
["Granville Island Parking Lot", "none", "Cartwright at Johnston", "Johnston at Old Bridge"],
"You are at the east side of Johnston Street. To the east is Cartwright Street and to the west is Old Bridge Street. To the north is a parking lot.",
["Seagull"],
"Granville Island")

johnston_at_old_bridge = Room("Johnston at Old Bridge",
["Johnston Street East", "Johnston Street Centre"],
["none", "none", "Johnston Street East", "Johnston Street Centre"],
"You are at the intersection of Johnston Street and Old Bridge Street.",
["Seagull"],
"Granville Island")

johnston_street_centre = Room("Johnston Street Centre", 
["Johnston at Old Bridge", "Johnston at Anderson"],
["none", "none", "Johnston at Old Bridge", "Johnston at Anderson"],
"You are at the central section of Johnston Street. To the east is Old Bridge Street and to the west is Anderson Street.",
["Seagull"],
"Granville Island")

johnston_at_anderson = Room("Johnston at Anderson", 
["Anderson Street Granville Island", "Johnston Street Centre", "Johnston Street West"],
["none", "Anderson Street Granville Island", "Johnston Street Centre", "Johnston Street West"],
"You are at the intersection of Johnston Street and Anderson Street.",
["Seagull"],
"Granville Island")

johnston_street_west = Room("Johnston Street West",
["Johnston at Anderson", "Johnston at Duranleau", "Granville Island Public Market"],
["Granville Island Public Market", "none", "Johnston at Anderson", "Johnston at Duranleau"],
"You are at the west side of Johnston Street. To the east is Anderson Street and to the west is Duranleau Street. To the north is a market.",
["Seagull"],
"Granville Island")

johnston_at_duranleau = Room("Johnston at Duranleau", 
["Duranleau Street", "Johnston Street West"],
["none", "Duranleau Street", "Johnston Street West", "none"],
"You are at the intersection of Johnston Street and Duranleau Street.",
["Seagull"],
"Granville Island")

duranleau_street = Room("Duranleau Street",
["Johnston at Duranleau", "Cartwright at Anderson", "YuBot Bank Granville Island"],
["Johnston at Duranleau", "none", "Cartwright at Anderson", "YuBot Bank Granville Island"],
"You are on a very short winding road. To the north is Johnston Street and to the east is Anderson Street. To the west is a bank.",
["Seagull"],
"Granville Island")

granville_island_public_market = Room("Granville Island Public Market",
["Johnston Street West"],
["none", "Johnston Street West", "none", "none"],
"You are in a market on Granville Island. There is a vendor here with free food samples in a fridge.",
[],
"Granville Island")

yubot_bank_granville_island = Room("YuBot Bank Granville Island", 
["Duranleau Street"], 
["none", "none", "Duranleau Street", "none"], 
"You are at the Granville Island branch of the YuBot bank. To the east is Duranleau Street.", 
[], 
"Granville Island")

yubot_gift_shop_granville_island = Room("YuBot Gift Shop Granville Island", 
["Cartwright Street West"], 
["Cartwright Street West", "none", "none", "none"], 
"You are in a small gift shop. To the north is Cartwright Street. There is a sign here that says:\n\nAvailable for 50 coins:📣\nAvailable for 50 coins:🔦\nAvailable for 5000 coins:📇", 
[], 
"Granville Island")

granville_island_parking_lot = Room("Granville Island Parking Lot",
["Johnston Street East"],
["none", "Johnston Street East", "none", "none"],
"You are in an empty parking lot on Granville Island. There is a box here.",
["Actor"],
"Granville Island",
"📝")


#----------------End of Granville Island Rooms---------------

olympic_village_station = Room("Olympic Village Station",
["500 Block 2nd Avenue"],
["none", "500 Block 2nd Avenue", "none", "none"],
"You are in the Olympic Village Canada Line Station. There is an info table here with a fridge on it. To the south is 2nd Avenue.",
[],
"False Creek South")

second_avenue_500_block = Room("500 Block 2nd Avenue",
["Olympic Village Station", "2nd at Cambie"],
["Olympic Village Station", "none", "2nd at Cambie", "none"],
"You are at the 500 block of an east-west road. To the north is a Canada Line Station and to the east is Cambie Street. There are bus stops here for\n\n50\n84",
[],
"False Creek South")

second_at_cambie = Room("2nd at Cambie",
["500 Block 2nd Avenue", "2100 Block Cambie Street"],
["none", "2100 Block Cambie Street", "none", "500 Block 2nd Avenue"],
"You are at the intersection of 2nd Avenue and Cambie Street.",
[],
"False Creek South")

cambie_street_2100_block = Room("2100 Block Cambie Street",
["2nd at Cambie", "6th at Cambie", "YuBot Bank False Creek South"],
["2nd at Cambie", "6th at Cambie", "none", "YuBot Bank False Creek South"],
"You are at the 2100 block of a north-south road. To the north is 2nd Avenue and to the south is 6th Avenue. To the west is a bank.",
[],
"False Creek South")

sixth_at_cambie = Room("6th at Cambie",
["2200 Block Cambie Street", "2100 Block Cambie Street"],
["2100 Block Cambie Street", "2200 Block Cambie Street", "none", "none"],
"You are at the intersection of 6th Avenue and Cambie Street.",
[],
"False Creek South")

cambie_street_2200_block = Room("2200 Block Cambie Street",
["7th at Cambie", "6th at Cambie", "YuBot Gift Shop False Creek South"],
["6th at Cambie", "7th at Cambie", "YuBot Gift Shop False Creek South", "none"],
"You are at the 2200 block of a north-south road. To the north is 6th Avenue and to the south is 7th Avenue. To the east is a gift shop.",
[],
"False Creek South")

seventh_at_cambie = Room("7th at Cambie",
["2200 Block Cambie Street", "2300 Block Cambie Street"],
["2200 Block Cambie Street", "2300 Block Cambie Street", "none", "none"],
"You are at the intersection of 7th Avenue and Cambie Street.",
[],
"False Creek South")

cambie_street_2300_block = Room("2300 Block Cambie Street",
["7th at Cambie", "8th at Cambie", "rqSHOP False Creek South"],
["7th at Cambie", "8th at Cambie", "none", "rqSHOP False Creek South"],
"You are at the 2300 block of a north-south road. To the north is 7th Avenue and to the south is 8th Avenue. To the west is a trinket shop.",
[],
"False Creek South")

eighth_at_cambie = Room("8th at Cambie",
["2400 Block Cambie Street", "2300 Block Cambie Street"],
["2300 Block Cambie Street", "2400 Block Cambie Street", "none", "none"],
"You are at the intersection of 8th Avenue and Cambie Street.",
[],
"False Creek South")

cambie_street_2400_block = Room("2400 Block Cambie Street",
["Broadway at Cambie", "8th at Cambie", "RQ Storage Solutions False Creek South"],
["8th at Cambie", "Broadway at Cambie", "RQ Storage Solutions False Creek South", "none"],
"You are at the 2400 block of a north-south road. To the north is 8th Avenue and to the south is Broadway. To the east is a storage shop.",
[],
"False Creek South")

broadway_at_cambie = Room("Broadway at Cambie",
["2400 Block Cambie Street", "Broadway-City Hall Station"],
["2400 Block Cambie Street", "Broadway-City Hall Station", "none", "none"],
"You are at the intersection of Broadway and Cambie Street. To the south is a Canada Line Station. There is a bus stop here for\n\n99",
[],
"False Creek South")

broadway_city_hall_station = Room("Broadway-City Hall Station",
["Broadway at Cambie"],
["Broadway at Cambie", "none", "none", "none"],
"You are in the Broadway-City Hall Canada Line Station. To the north is Broadway.",
[],
"False Creek South")

fifty = Room("50",
["Lamey's Mill at Anderson", "500 Block 2nd Avenue"],
["none", "none", "none", "none"],
"You are in a bus running route 50. You can go to the following destinations:\n\n"+"\n".join(["Lamey's Mill at Anderson", "500 Block 2nd Avenue"]),
[],
"False Creek South")

yubot_bank_false_creek_south = Room("YuBot Bank False Creek South", 
["2100 Block Cambie Street"], 
["none", "none", "2100 Block Cambie Street", "none"], 
"You are at the False Creek South branch of the YuBot bank. To the east is Cambie Street.", 
[], 
"False Creek South")

yubot_gift_shop_false_creek_south = Room("YuBot Gift Shop False Creek South", 
["2200 Block Cambie Street"], 
["none", "none", "none", "2200 Block Cambie Street"], 
"You are in a small gift shop. To the west is Cambie Street. There is a sign here that says:\n\nAvailable for 50 coins:📣\nAvailable for 50 coins:🔦\nAvailable for 5000 coins:📇", 
[], 
"False Creek South")

rqshop_false_creek_south = Room("rqSHOP False Creek South",
["2300 Block Cambie Street"],
["none", "none", "2300 Block Cambie Street", "none"],
"You are in a small trinket shop. To the east is Cambie Street. There is a sign here that says:\n\nAvailable for 50000 coins:💳",
[], 
"False Creek South")

rqstorage_false_creek_south = Room("RQ Storage Solutions False Creek South",
["2400 Block Cambie Street"],
["none", "none", "none", "2400 Block Cambie Street"],
"You are in a small storage shop. To the west is Cambie Street. There is a sign here that says:\n\nAvailable for 7000 coins:👜\nAvailable for 100000 coins:🛄",
[], 
"False Creek South")

ninety_nine = Room("99",
["UBC Bus Loop", "Broadway at Cambie"],
["none", "none", "none", "none"],
"You are in a bus running route 99. You can go to the following destinations:\n\n"+"\n".join(["UBC Bus Loop", "Broadway at Cambie"]),
[],
"False Creek South")

#-------------End of False Creek South Rooms-----------------
forty_first_at_granville = Room("41st at Granville",
["none", "Driveway", "Food Cart 41st/Granville", "YuBot Bank 41st @ Granville"],
None,
"You are at the intersection of 41st and Granville. To the south is an empty driveway, to the west is a bank and to the east is a food cart. There are bus stops here for\n\n10\n43",
[],
"41st @ Granville")

yubot_bank_41st_granville = Room("YuBot Bank 41st @ Granville",  
["none", "none", "41st at Granville", "none"], 
None,
"You are at the 41st @ Granville branch of the YuBot bank. To the east is Granville Street.", 
[], 
"41st @ Granville")

food_cart_41st_granville = Room("Food Cart 41st/Granville",
["none", "none", "none", "41st at Granville"],
None,
"You are at a food cart on the side of 41st Avenue. There is a fridge here. To the west is Granville Street.",
[],
"41st @ Granville")

driveway = Room("Driveway",
["41st at Granville", "none", "none", "none"],
None,
"You are on a driveway just south of 41st Avenue. There is a box here.",
["Pigeon Flock"],
"41st @ Granville",
"🥖")

forty_three = Room("43",
["UBC Bus Loop", "41st at West Boulevard", "41st at Granville", "41st at Cambie"],
["none", "none", "none", "none"],
"You are in a bus running route 43. You can go to the following destinations:\n\n"+"\n".join(["UBC Bus Loop", "41st at West Boulevard", "41st at Granville", "41st at Cambie"]),
[],
"41st @ Granville")

#------------End of 41st @ Granville Rooms------------------

arbutus_greenway = Room("Arbutus Greenway", 
["none", "41st at West Boulevard", "none", "none"],
None,
"You are on a wide path in Kerrisdale. There is a fridge on a table here.",
[],
"Kerrisdale")

forty_first_at_west_blvd = Room("41st at West Boulevard",
["Arbutus Greenway", "5700 Block West Boulevard", "none", "2100 Block 41st Avenue"],
None,
"You are at the intersection of 41st Avenue and West Boulevard. To the north is a wide path. There is a bus stop here for\n\n43",
[],
"Kerrisdale")

west_boulevard_5700_block = Room("5700 Block West Boulevard",
["41st at West Boulevard", "42nd at West Boulevard", "none", "none"],
None,
"You are at the 5700 block of a north-south road. To the north is 41st Avenue and to the south is 42nd Avenue.",
["Pigeon"],
"Kerrisdale")

forty_second_at_west_blvd = Room("42nd at West Boulevard",
["5700 Block West Boulevard", "none", "none", "Vancouver Public Library Kerrisdale Branch"],
None,
"You are at the intersection of 42nd Avenue and West Boulevard. To the west is a library.",
["Pigeon"],
"Kerrisdale")

vancouver_public_library_kerrisdale_branch = Room("Vancouver Public Library Kerrisdale Branch", 
["none", "none", "42nd at West Boulevard", "none"], 
None,
"You are in a library. There are books here. There is an exit to the east here.", 
[], 
"Kerrisdale")

forty_first_2100_block = Room("2100 Block 41st Avenue",
["none", "none", "41st at West Boulevard", "41st at Yew"],
None,
"You are at the 2100 block of an east-west road. To the east is West Boulevard and to the west is Yew Street.",
["Pigeon"],
"Kerrisdale")

forty_first_at_yew = Room("41st at Yew",
["none", "none", "2100 Block 41st Avenue", "2200 Block 41st Avenue"],
None,
"You are at the intersection of 41st Avenue and Yew Street.",
["Pigeon"],
"Kerrisdale")

forty_first_2200_block = Room("2200 Block 41st Avenue",
["none", "YuBot Gift Shop Kerrisdale", "41st at Yew", "41st at Vine"],
None,
"You are at the 2200 block of an east-west road. To the east is Yew Street and to the west is Vine Street. To the south is a gift shop.",
["Pigeon"],
"Kerrisdale")

yubot_gift_shop_kerrisdale = Room("YuBot Gift Shop Kerrisdale", 
["2200 Block 41st Avenue", "none", "none", "none"], 
None,
"You are in a small gift shop. To the north is 41st Avenue. There is a sign here that says:\n\nAvailable for 50 coins:📣\nAvailable for 50 coins:🔦\nAvailable for 5000 coins:📇", 
[], 
"Kerrisdale")

forty_first_at_vine = Room("41st at Vine",
["none", "none", "2200 Block 41st Avenue", "2300 Block 41st Avenue"],
None,
"You are at the intersection of 41st Avenue and Vine Street.",
["Pigeon"],
"Kerrisdale")

forty_first_2300_block = Room("2300 Block 41st Avenue",
["rqSHOP Kerrisdale", "none", "41st at Vine", "41st at Balsam"],
None,
"You are at the 2300 block of an east-west road. To the east is Vine Street and to the west is Balsam Street. To the north is a trinket shop.",
["Pigeon"],
"Kerrisdale")

rqshop_kerrisdale = Room("rqSHOP Kerrisdale",
["none", "2300 Block 41st Avenue", "none", "none"],
None,
"You are in a small trinket shop. To the south is 41st Avenue. There is a sign here that says:\n\nAvailable for 200000 coins:♨",
[], 
"Kerrisdale")

forty_first_at_balsam = Room("41st at Balsam",
["none", "none", "2300 Block 41st Avenue", "2400 Block 41st Avenue"],
None,
"You are at the intersection of 41st Avenue and Balsam Street.",
["Pigeon"],
"Kerrisdale")

forty_first_2400_block = Room("2400 Block 41st Avenue",
["none", "none", "41st at Balsam", "41st at Larch"],
None,
"You are at the 2400 block of an east-west road. To the east is Balsam Street and to the west is Larch Street.",
["Pigeon"],
"Kerrisdale")

forty_first_at_larch = Room("41st at Larch",
["YuBot Bank Kerrisdale", "Elm Park", "2400 Block 41st Avenue", "none"],
None,
"You are at the intersection of 41st Avenue and Larch Street. To the north is a bank and to the south is a park.",
["Pigeon"],
"Kerrisdale")

yubot_bank_kerrisdale = Room("YuBot Bank Kerrisdale",  
["none", "41st at Larch", "none", "none"], 
None,
"You are at the Kerrisdale branch of the YuBot bank. To the south is 41st Avenue.", 
[], 
"Kerrisdale")

elm_park = Room("Elm Park",
["41st at Larch", "none", "none", "none"],
None,
"You are at a small park just south of 41st Avenue. There is a box here.",
["Athlete"],
"Kerrisdale",
"🍃")






#--------------------End of Kerrisdale Rooms-----------------

forty_first_at_cambie = Room("41st at Cambie",
["YuBot Bank Oakridge", "Oakridge-41st Station", "none", "none"],
None,
"You are at the intersection of 41st Avenue and Cambie. To the north is a bank and to the south is a Canada Line Station. There is a bus stop here for\n\n43",
[],
"Oakridge")

oakridge_41st_station = Room("Oakridge-41st Station",
["41st at Cambie", "none", "none", "none"],
None,
"You are in the Oakridge-41st Canada Line Station. There is an info table here with a fridge on it. To the north is 41st Avenue.",
[],
"Oakridge")

yubot_bank_oakridge = Room("YuBot Bank Oakridge",  
["none", "41st at Cambie", "none", "none"], 
None,
"You are at the Oakridge branch of the YuBot bank. To the south is 41st Avenue.", 
[], 
"Oakridge")


canada_line = Room("Canada Line",
["Waterfront Station", "Vancouver City Centre Station", "Olympic Village Station", "Broadway-City Hall Station", "Oakridge-41st Station", "Marine Drive Station", "Bridgeport Station", "Aberdeen Station", "Lansdowne Station", "Brighouse Station"],
["none", "none", "none", "none"],
"You are in an above-ground subway train running a route called the Canada Line. You can go to the following destinations:\n\n"+"\n".join(["Waterfront Station", "Vancouver City Centre Station", "Olympic Village Station", "Broadway-City Hall Station", "Oakridge-41st Station", "Marine Drive Station", "Bridgeport Station", "Aberdeen Station", "Lansdowne Station", "Brighouse Station"]),
[],
"Oakridge")



#--------------------End of Oakridge Rooms-------------------

marine_at_cambie = Room("Marine at Cambie",
["YuBot Bank Marine Drive", "Marine Drive Station", "Marine Drive Open Space", "none"],
None,
"You are at the intersection of Marine Drive and Cambie Street. To the north is a bank, to the south is a Canada Line Station and to the east is an open space. There is a bus stop here for\n\n10",
[],
"Marine Drive")

marine_drive_station = Room("Marine Drive Station",
["Marine at Cambie", "none", "none", "none"],
None,
"You are in the Marine Drive Canada Line Station. There is an info table here with a fridge on it. To the north is Marine Drive.",
[],
"Marine Drive")

yubot_bank_marine_drive = Room("YuBot Bank Marine Drive",  
["none", "Marine at Cambie", "none", "none"], 
None,
"You are at the Marine Drive branch of the YuBot bank. To the south is Marine Drive.", 
[], 
"Marine Drive")

marine_drive_open_space = Room("Marine Drive Open Space",
["none", "none", "none", "Marine at Cambie"],
None,
"You are in an open space on Marine Drive. There is a box here.",
["Duck"],
"Marine Drive",
"🌱")
#------------------End of Marine Drive Rooms-----------------


pipeline_at_stanley_park = Room("Pipeline at Stanley Park",
["Pipeline Road", "none", "none", "North Lagoon Drive"],
None,
"You are at the intersection of Pipeline Road and Stanley Park Drive. There is a bus stop here for\n\n19",
[],
"Stanley Park")

nineteen = Room("19",
["Pender at Granville", "Pipeline at Stanley Park", "Stanley Park Loop"],
["none", "none", "none", "none"],
"You are in a bus running route 19. You can go to the following destinations:\n\n"+"\n".join(["Pender at Granville", "Pipeline at Stanley Park", "Stanley Park Loop"]),
[],
"Stanley Park")

pipeline_road = Room("Pipeline Road",
["Stanley Park Loop", "Pipeline at Stanley Park", "none", "none"],
None,
"You are on a north-south road through a tall forest. To the north is a small loop and to the south is Stanley Park Drive.",
["Crow"],
"Stanley Park")

stanley_park_loop = Room("Stanley Park Loop",
["none", "Pipeline Road", "none", "none"],
None,
"You are in a small loop in the middle of Stanley Park. There is a pavilion here with a fridge. There is a bus stop here for\n\n19",
[],
"Stanley Park")

north_lagoon_drive = Room("North Lagoon Drive",
["none", "none", "Pipeline at Stanley Park", "Tatlow at North Lagoon"],
None,
"You are on an east-west road by a lagoon. To the east is Pipeline Road and to the west is a small trail.",
["Crow"],
"Stanley Park")

tatlow_at_north_lagoon = Room("Tatlow at North Lagoon",
["Stanley Park-Maze Entrance", "none", "North Lagoon Drive", "Tatlow Walk"],
None,
"You are at the intersection of a small trail and North Lagoon Drive. To the north is the entrance to a maze.",
["Crow"],
"Stanley Park")

tatlow_walk = Room("Tatlow Walk",
["none", "none", "Tatlow at North Lagoon", "Third Beach"],
None,
"You are on a small east-west trail. To the east is North Lagoon Drive and to the west is a beach.",
["Crow"],
"Stanley Park")


third_beach = Room("Third Beach",
["none", "none", "Tatlow Walk", "none"],
None,
"You are at a beach on the west end of Stanley Park. To the east is a small trail. There is a box here.",
["Obese Crow"],
"Stanley Park",
"🍩")

stanley_park_maze_entrance = Room("Stanley Park-Maze Entrance",
["Stanley Park Maze 0", "Tatlow at North Lagoon", "none", "none"],
None,
"You are at the entrance to the Stanley Park Maze. The maze is north of here. If you are about to enter, this is your last chance to get out. If you have just exited, congratulations. To the south is North Lagoon Drive.",
["Crow"],
"Stanley Park")

sm0 = Room("Stanley Park Maze 0",
["Stanley Park-Maze Entrance", "Stanley Park Maze 1", "Stanley Park Maze 2", "Stanley Park Maze 3", "Stanley Park Maze 4", "Stanley Park Maze 5", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm1 = Room("Stanley Park Maze 1",
["none", "Stanley Park Maze 0", "Stanley Park Maze 2", "Stanley Park Maze 3", "Stanley Park Maze 4", "Stanley Park Maze 5", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm2 = Room("Stanley Park Maze 2",
["none", "Stanley Park Maze 0", "Stanley Park Maze 1", "Stanley Park Maze 3", "Stanley Park Maze 4", "Stanley Park Maze 5", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm3 = Room("Stanley Park Maze 3",
["none", "Stanley Park Maze 0", "Stanley Park Maze 2", "Stanley Park Maze 1", "Stanley Park Maze 4", "Stanley Park Maze 5", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm4 = Room("Stanley Park Maze 4",
["Stanley Park Maze 0", "Stanley Park Maze 2", "Stanley Park Maze 3", "Stanley Park Maze 1", "Stanley Park Maze 5", "none", "none", "none", "none", "Stanley Park Maze 10"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm5 = Room("Stanley Park Maze 5",
["none", "Stanley Park Maze 0", "Stanley Park Maze 2", "Stanley Park Maze 3", "Stanley Park Maze 4", "Stanley Park Maze 1", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

#----------------------------

sm6 = Room("Stanley Park Maze 6",
["none", "Stanley Park Maze 11", "Stanley Park Maze 7", "Stanley Park Maze 8", "Stanley Park Maze 9", "Stanley Park Maze 10", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm7 = Room("Stanley Park Maze 7",
["Stanley Park Maze 11", "Stanley Park Maze 6", "Stanley Park Maze 8", "Stanley Park Maze 9", "Stanley Park Maze 10", "none", "none", "none", "none", "Stanley Park Maze 14"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm8 = Room("Stanley Park Maze 8",
["none", "Stanley Park Maze 11", "Stanley Park Maze 7", "Stanley Park Maze 6", "Stanley Park Maze 9", "Stanley Park Maze 10", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm9 = Room("Stanley Park Maze 9",
["none", "Stanley Park Maze 11", "Stanley Park Maze 7", "Stanley Park Maze 8", "Stanley Park Maze 6", "Stanley Park Maze 10", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm10 = Room("Stanley Park Maze 10",
["Stanley Park Maze 11", "Stanley Park Maze 7", "Stanley Park Maze 8", "Stanley Park Maze 9", "Stanley Park Maze 6", "none", "none", "none", "none", "Stanley Park Maze 4"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm11 = Room("Stanley Park Maze 11",
["none", "Stanley Park Maze 6", "Stanley Park Maze 7", "Stanley Park Maze 8", "Stanley Park Maze 9", "Stanley Park Maze 10", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

#------------

sm12 = Room("Stanley Park Maze 12",
["none", "Stanley Park Maze 13", "Stanley Park Maze 14", "Stanley Park Maze 15", "Stanley Park Maze 16", "Stanley Park Maze 17", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm13 = Room("Stanley Park Maze 13",
["none", "Stanley Park Maze 12", "Stanley Park Maze 14", "Stanley Park Maze 15", "Stanley Park Maze 16", "Stanley Park Maze 17", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm14 = Room("Stanley Park Maze 14",
["Stanley Park Maze 13", "Stanley Park Maze 12", "Stanley Park Maze 15", "Stanley Park Maze 16", "Stanley Park Maze 17", "none", "none", "none", "none", "Stanley Park Maze 7"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm15 = Room("Stanley Park Maze 15",
["none", "Stanley Park Maze 13", "Stanley Park Maze 14", "Stanley Park Maze 12", "Stanley Park Maze 16", "Stanley Park Maze 17", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm16 = Room("Stanley Park Maze 16",
["Stanley Park Maze 13", "Stanley Park Maze 14", "Stanley Park Maze 15", "Stanley Park Maze 12", "Stanley Park Maze 17", "none", "none", "none", "none", "Stanley Park Maze 21"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm17 = Room("Stanley Park Maze 17",
["none", "Stanley Park Maze 13", "Stanley Park Maze 14", "Stanley Park Maze 15", "Stanley Park Maze 16", "Stanley Park Maze 12", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

#---------------------------

sm18 = Room("Stanley Park Maze 18",
["none", "Stanley Park Maze 19", "Stanley Park Maze 20", "Stanley Park Maze 21", "Stanley Park Maze 22", "Stanley Park Maze 23", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow Flock"],
"Stanley Park")

sm19 = Room("Stanley Park Maze 19",
["none", "Stanley Park Maze 18", "Stanley Park Maze 20", "Stanley Park Maze 21", "Stanley Park Maze 22", "Stanley Park Maze 23", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm20 = Room("Stanley Park Maze 20",
["none", "Stanley Park Maze 19", "Stanley Park Maze 18", "Stanley Park Maze 21", "Stanley Park Maze 22", "Stanley Park Maze 23", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm21 = Room("Stanley Park Maze 21",
["Stanley Park Maze 16", "Stanley Park Maze 19", "Stanley Park Maze 20", "Stanley Park Maze 18", "Stanley Park Maze 22", "Stanley Park Maze 23", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm22 = Room("Stanley Park Maze 22",
["none", "Stanley Park Maze 19", "Stanley Park Maze 20", "Stanley Park Maze 21", "Stanley Park Maze 18", "Stanley Park Maze 23", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

sm23 = Room("Stanley Park Maze 23",
["none", "Stanley Park Maze 19", "Stanley Park Maze 20", "Stanley Park Maze 21", "Stanley Park Maze 22", "Stanley Park Maze 18", "none", "none", "none", "none"],
None,
"You are in the Stanley Park Maze. All paths seem the same.",
["Crow"],
"Stanley Park")

'''
0 1 2 3 4 5 (4-10)
6 7 8 9 10 11 (7-14)
12 13 14 15 16 17(16-21)
18 19 20 21 22 23 (18)
'''

#------------------End of Stanley Park Rooms-----------------
#------------------------------------------------------------
#--------------------END OF VANCOUVER REGION-----------------
#------------------------------------------------------------

bridgeport_station = Room("Bridgeport Station",
["none", "none", "none", "Bridgeport Station Bus Loop"],
None,
"You are in the Bridgeport Canada Line station. There is a fridge here on an info table. To the west is a looping road with buses.",
[],
"Bridgeport")

bridgeport_bus_loop = Room("Bridgeport Station Bus Loop",
["none", "none", "Bridgeport Station", "none"],
None,
"You are at the Bridgeport bus loop. To the east is a Canada Line station. There are bus stops here for\n\n403\n480\n601",
[],
"Bridgeport")

four_eighty = Room("480",
["UBC Bus Loop", "Bridgeport Station Bus Loop"],
["none", "none", "none", "none"],
"You are in a bus running route 480. You can go to the following destinations:\n\n"+"\n".join(["UBC Bus Loop", "Bridgeport Station Bus Loop"]),
[],
"Bridgeport")

aberdeen_station = Room("Aberdeen Station",
["none", "none", "none", "none"],
None,
"You are in the Aberdeen Canada Line station. There are bus stops here for\n\n403\n410",
[],
"Bridgeport")

#-----------------End of Bridgeport Rooms--------------------

entertainment_boulevard = Room("Entertainment Boulevard", 
["Entertainment Roundabout", "Steveston at Entertainment", "Bowling Entrance", "Theatres"],
None,
"You are on Entertainment Boulevard. To the north is a roundabout and to the south is Steveston Highway. There is a movie theatre to the west and a bowling alley to the east.",
["Pigeon"],
"Riverport")

entertainment_roundabout = Room("Entertainment Roundabout",
["none", "Entertainment Boulevard", "none", "none"],
None,
"You are at a roundabout on the north end of Entertainment Boulevard. There is a bus stop here for\n\n403",
[],
"Riverport")

steveston_at_entertainment = Room("Steveston at Entertainment",
["Entertainment Boulevard", "YuBot Bank Riverport", "none", "none"],
None,
"You are at the intersection of Steveston Highway and Entertainment Boulevard. To the south is a bank.",
["Pigeon"],
"Riverport")

yubot_bank_riverport = Room("YuBot Bank Riverport",  
["Steveston at Entertainment", "none", "none", "none"], 
None,
"You are at the Riverport branch of the YuBot bank. To the north is Steveston Highway.", 
[], 
"Riverport")

theatres = Room("Theatres", 
["none", "none", "Entertainment Boulevard", "none"],
None,
"You are in a movie theatre. To the side is a kiosk with free samples in a fridge. To the east is Entertainment Boulevard.",
[],
"Riverport")

bowling_entrance = Room("Bowling Entrance",
["Bowling Shop", "none", "Bowling Alley", "Entertainment Boulevard"],
None,
"You are at the entrance to a bowling alley. To the west is Entertainment Boulevard. To the east is the alley and to the north is a shop.",
["Pigeon"],
"Riverport")

bowling_shop = Room("Bowling Shop",
["none", "Bowling Entrance", "none", "none"],
None,
"You are in a small shop at a bowling alley. There is a sign here that says:\n\n🎟: 500 coins\n🎱: 100 coins\n👟: 50 coins\n🎳: 25000 coins",
[],
"Riverport")

bowling_alley = Room("Bowling Alley",
["none", "none", "none", "Bowling Entrance"],
None,
"You are at a bowling alley. There is a scanner for tickets here.",
[],
"Riverport")

four_hundred_three = Room("403",
["Entertainment Roundabout", "Granville at No. 3", "Cook at No. 3", "Westminster at No. 3", "Lansdowne at No. 3", "Aberdeen Station", "Bridgeport Station Bus Loop"],
["none", "none", "none", "none"],
"You are in a bus running route 403. You can go to the following destinations:\n\n"+"\n".join(["Entertainment Roundabout", "Granville at No. 3", "Cook at No. 3", "Westminster at No. 3", "Lansdowne at No. 3", "Aberdeen Station", "Bridgeport Station Bus Loop"]),
[],
"Riverport")

#-----------------End of Riverport Rooms---------------------


lansdowne_station = Room("Lansdowne Station",
["none", "Lansdowne at No. 3", "none", "none"],
None,
"You are at the Lansdowne Canada Line station. To the south is Lansdowne Road.",
[],
"Brighouse")

lansdowne_at_no_3 = Room("Lansdowne at No. 3",
["Lansdowne Station", "5700 Block No. 3 Road", "8100 Block Lansdowne Road", "none"],
None,
"You are at the intersection of Lansdowne Road and No. 3 Road. To the north is a Canada Line station. There is a bus stop here for \n\n403",
[],
"Brighouse")

lansdowne_road_8100_block = Room("8100 Block Lansdowne Road",
["none", "none", "Lansdowne at Cooney", "Lansdowne at No. 3"],
None,
"You are at the 8100 block of an east-west road. To the east is Cooney Road and to the west is No. 3 Road.",
npclist,
"Brighouse")

lansdowne_at_cooney = Room("Lansdowne at Cooney",
["none", "5500 Block Cooney Road", "8400 Block Lansdowne Road", "8100 Block Lansdowne Road"],
None,
"You are at the intersection of Lansdowne Road and Cooney Road.",
npclist,
"Brighouse")


lansdowne_road_8400_block = Room("8400 Block Lansdowne Road",
["none", "none", "Lansdowne at Arcadia", "Lansdowne at Cooney"],
None,
"You are at the 8400 block of an east-west road. To the east is Arcadia Road and to the west is Cooney Road.",
npclist,
"Brighouse")

lansdowne_at_arcadia = Room("Lansdowne at Arcadia",
["none", "5400 Block Arcadia Road", "8900 Block Lansdowne Road", "8400 Block Lansdowne Road"],
None,
"You are at the intersection of Lansdowne Road and Arcadia Road.",
npclist,
"Brighouse")

lansdowne_road_8900_block = Room("8900 Block Lansdowne Road",
["none", "none", "Lansdowne at Garden City", "Lansdowne at Arcadia"],
None,
"You are at the 8900 block of an east-west road. To the east is Garden City Road and to the west is Arcadia Road.",
npclist,
"Brighouse")

lansdowne_at_garden_city = Room("Lansdowne at Garden City",
["none", "5500 Block Garden City Road", "none", "8900 Block Lansdowne Road"],
None,
"You are at the intersection of Lansdowne Road and Garden City Road.",
npclist,
"Brighouse")

no_3_road_5700_block = Room("5700 Block No. 3 Road",
["Lansdowne at No. 3", "Ackroyd at No. 3", "none", "none"],
None,
"You are at the 5700 block of a central north-south road. To the north is Lansdowne Road and to the south is Ackroyd Road.",
npclist,
"Brighouse")

cooney_road_5500_block = Room("5500 Block Cooney Road",
["Lansdowne at Cooney", "Ackroyd at Cooney", "none", "none"],
None,
"You are at the 5500 block of a north-south road. To the north is Lansdowne Road and to the south is Ackroyd Road.",
npclist,
"Brighouse")

arcadia_road_5400_block = Room("5400 Block Arcadia Road",
["Lansdowne at Arcadia", "Ackroyd at Arcadia", "none", "none"],
None,
"You are at the 5400 block of a north-south road. To the north is Lansdowne Road and to the south is Ackroyd Road.",
npclist,
"Brighouse")

garden_city_5500_block = Room("5500 Block Garden City Road",
["Lansdowne at Garden City", "Garden City at Westminster", "Garden City Lands", "none"],
None,
"You are at the 5500 block of a north-south road. To the north is Lansdowne Road and to the south is Westminster Highway. To the east is a large expanse of grass.",
npclist,
"Brighouse")

ackroyd_at_no_3 = Room("Ackroyd at No. 3",
["5700 Block No. 3 Road", "5800 Block No. 3 Road", "8100 Block Ackroyd Road", "none"],
None,
"You are at the intersection of Ackroyd Road and No. 3 Road.",
npclist,
"Brighouse")

ackroyd_road_8100_block = Room("8100 Block Ackroyd Road",
["rqSHOP Brighouse", "none", "Ackroyd at Cooney", "Ackroyd at No. 3"],
None,
"You are at the 8100 block of an east-west road. To the east is Cooney Road and to the west is No. 3 Road. To the north is a trinket shop.",
npclist,
"Brighouse")

ackroyd_at_cooney = Room("Ackroyd at Cooney",
["5500 Block Cooney Road", "5800 Block Cooney Road", "8400 Block Ackroyd Road", "8100 Block Ackroyd Road"],
None,
"You are at the intersection of Ackroyd Road and Cooney Road.",
npclist,
"Brighouse")

ackroyd_road_8400_block = Room("8400 Block Ackroyd Road",
["none", "none", "Ackroyd at Arcadia", "Ackroyd at Cooney"],
None,
"You are at the 8400 block of an east-west road. To the east is Arcadia Road and to the west is Cooney Road.",
npclist,
"Brighouse")

ackroyd_at_arcadia = Room("Ackroyd at Arcadia",
["5400 Block Arcadia Road", "5700 Block Arcadia Road", "none", "8400 Block Ackroyd Road"],
None,
"You are at the intersection of Ackroyd Road and Arcadia Road. There is a box here.",
["Actor Redux"],
"Brighouse",
"✏")

no_3_road_5800_block = Room("5800 Block No. 3 Road",
["Ackroyd at No. 3", "Westminster at No. 3", "none", "none"],
None,
"You are at the 5800 block of a central north-south road. To the north is Ackroyd Road and to the south is Westminster Highway.",
npclist,
"Brighouse")

cooney_road_5800_block = Room("5800 Block Cooney Road",
["Ackroyd at Cooney", "Westminster at Cooney", "none", "none"],
None,
"You are at the 5800 block of a north-south road. To the north is Ackroyd Road and to the south is Wesminster Highway.",
npclist,
"Brighouse")

arcadia_road_5700_block = Room("5700 Block Arcadia Road",
["Ackroyd at Arcadia", "Westminster at Arcadia", "none", "none"],
None,
"You are at the 5700 block of a north-south road. To the north is Ackroyd Road and to the south is Westminster Highway.",
npclist,
"Brighouse")

westminster_at_no_3 = Room("Westminster at No. 3",
["5800 Block No. 3 Road", "6000 Block No. 3 Road", "8100 Block Westminster Highway", "YuBot Bank Brighouse"],
None,
"You are at the intersection of Westminster Highway and No. 3 Road. To the west is a bank. There is a bus stop here for\n\n403",
[],
"Brighouse")

westminster_highway_8100_block = Room("8100 Block Westminster Highway",
["none", "none", "Westminster at Buswell", "Westminster at No. 3"],
None,
"You are at the 8100 block of an east-west road. To the east is Buswell Street and to the west is No. 3 Road.",
npclist,
"Brighouse")

westminster_at_buswell = Room("Westminster at Buswell",
["none", "6100 Block Buswell Street", "8200 Block Westminster Highway", "8100 Block Westminster Highway"],
None,
"You are at the intersection of Westminster Highway and Buswell Street.",
npclist,
"Brighouse")

westminster_highway_8200_block = Room("8200 Block Westminster Highway", 
["none", "none", "Westminster at Cooney", "Westminster at Buswell"],
None,
"You are at the 8200 block of an east-west road. To the east is Cooney Road and to the west is Buswell Street.",
npclist,
"Brighouse")

westminster_at_cooney = Room("Westminster at Cooney",
["5800 Block Cooney Road", "6100 Block Cooney Road", "8400 Block Westminster Highway", "8200 Block Westminster Highway"],
None,
"You are at the intersection of Westminster Highway and Cooney Road.",
npclist,
"Brighouse")

westminster_highway_8400_block = Room("8400 Block Westminster Highway",
["none", "none", "Westminster at Arcadia", "Westminster at Cooney"],
None,
"You are at the 8400 block of an east-west road. To the east is Arcadia Road and to the west is Cooney Road.",
npclist,
"Brighouse")

westminster_at_arcadia = Room("Westminster at Arcadia",
["5700 Block Arcadia Road", "none", "8800 Block Westminster Highway", "8400 Block Westminster Highway"],
None,
"You are at the intersection of Westminster Highway and Arcadia Road.",
npclist,
"Brighouse")

westminster_highway_8800_block = Room("8800 Block Westminster Highway",
["none", "none", "Westminster at Garden City", "Westminster at Arcadia"],
None,
"You are at the 8800 block of an east-west road. To the west is Arcadia Road and to the east is Garden City Road.",
npclist,
"Brighouse")

westminster_at_garden_city = Room("Westminster at Garden City",
["5500 Block Garden City Road", "6300 Block Garden City Road", "none", "8800 Block Westminster Highway"],
None,
"You are at the intersection of Westminster Highway and Garden City Road.",
npclist,
"Brighouse")

no_3_road_6000_block = Room("6000 Block No. 3 Road", 
["Westminster at No. 3", "Saba at No. 3", "none", "none"],
None,
"You are at the 6000 block of a central north-south road. To the north is Westminster Highway and to the south is Saba Road.",
npclist,
"Brighouse")

buswell_street_6100_block = Room("6100 Block Buswell Street",
["Westminster at Buswell", "Saba at Buswell", "none", "none"],
None,
"You are at the 6100 block of a north-south road. To the north is Westminster Highway and to the south is Saba Road.",
npclist,
"Brighouse")

cooney_road_6100_block = Room("6100 Block Cooney Road",
["Westminster at Cooney", "Saba at Cooney", "none", "none"],
None,
"You are at the 6100 block of a north-south road. To the north is Westminster Highway and to the south is Saba Road.",
npclist,
"Brighouse")

garden_city_6300_block = Room("6300 Block Garden City Road", 
["Westminster at Garden City", "Cook at Garden City", "none", "none"],
None,
"You are at the 6300 block of a north-south road. To the north is Westminster Highway and to the south is Cook Road.",
npclist,
"Brighouse")

saba_at_no_3 = Room("Saba at No. 3",
["6000 Block No. 3 Road", "6300 Block No. 3 Road", "8000 Block Saba Road", "none"],
None,
"You are at the intersection of Saba Road and No. 3 Road.",
npclist,
"Brighouse")

saba_road_8000_block = Room("8000 Block Saba Road",
["none", "none", "Saba at Buswell", "Saba at No. 3"],
None,
"You are at the 8000 block of an east-west road. To the east is Buswell Street and to the west is No. 3 Road.",
npclist,
"Brighouse")

saba_at_buswell = Room("Saba at Buswell",
["6100 Block Buswell Street", "6300 Block Buswell Street",
"8200 Block Saba Road", "8000 Block Saba Road", "Lang Park"],
None,
"You are at the intersection of Saba Road and Buswell Street. There is a park here.",
npclist,
"Brighouse")

saba_road_8200_block = Room("8200 Block Saba Road",
["none", "none", "Saba at Cooney", "Saba at Buswell"],
None,
"You are at the 8200 block of an east-west road. To the east is Cooney Road and to the west is Buswell Street.",
npclist,
"Brighouse")

saba_at_cooney = Room("Saba at Cooney",
["6100 Block Cooney Road", "6300 Block Cooney Road", "Spires Gate", "8200 Block Saba Road"],
None,
"You are at the intersection of Saba Road and Cooney Road.",
npclist,
"Brighouse")

spires_gate = Room("Spires Gate",
["none", "none", "Spires Gate at Spires Road", "Saba at Cooney"],
None,
"You are on a short east-west road. To the west is Cooney Road and to the east is Spires Road.",
npclist,
"Brighouse")

spires_gate_at_road = Room("Spires Gate at Spires Road",
["Spires Road NW", "Spires Road WSW", "none", "Spires Gate"],
None,
"You are at the intersection of Spires Gate and Spires Road.",
npclist,
"Brighouse")

spires_road_nw = Room("Spires Road NW",
["Spires NW Corner", "Spires Gate at Spires Road", "none", "none"],
None,
"You are on the northwest section of a looping road. To the south is spires gate.",
npclist,
"Brighouse")

spires_nw_corner = Room("Spires NW Corner",
["none", "Spires Road NW", "Spires Road N", "none"],
None,
"You are at the NW corner of a looping road.",
npclist,
"Brighoue")

spires_road_n = Room("Spires Road N",
["none", "none", "Spires NE Corner", "Spires NW Corner"],
None,
"You are on the north section of a looping road.",
npclist,
"Brighouse")

spires_ne_corner = Room("Spires NE Corner",
["none", "Spires Road E", "none", "Spires Road N"],
None,
"You are at the NE corner of a looping road.",
npclist,
"Brighouse")

spires_road_e = Room("Spires Road E",
["Spires NE Corner", "Spires SE Corner", "none", "none"],
None,
"You are on the east section of a looping road.",
npclist,
"Brighouse")

spires_se_corner = Room("Spires SE Corner",
["Spires Road E", "none", "none", "Spires Road SE"],
None,
"You are at the SE corner of a looping road.",
npclist,
"Brighouse")

spires_road_se = Room("Spires Road SE",
["none", "none", "Spires SE Corner", "Spires E at Cook Crescent"],
None,
"You are on the SE section of a looping road. To the west is Cook Crescent",
npclist,
"Brighouse")

spires_e_cook = Room("Spires E at Cook Crescent",
["Cook Crescent E", "none", "Spires Road SE", "East Spires Road S"],
None,
"You are at the intersection of Spires Road and Cook Crescent.",
npclist,
"Brighouse")

e_spires_s = Room("East Spires Road S",
["none", "none", "Spires E at Cook Crescent", "Spires at Cook Gate"],
None,
"You are on the east southern section of a looping road. To the east is Cook Crescent and to the west is Cook Gate.",
npclist,
"Brighouse")

spires_at_cook_gate = Room("Spires at Cook Gate",
["none", "Cook Gate", "East Spires Road S", "West Spires Road S"],
None,
"You are at the intersection of Spires Road and Cook Gate.",
npclist,
"Brighouse")

w_spires_s = Room("West Spires Road S",
["none", "none", "Spires at Cook Gate", "Spires W at Cook Crescent"],
None,
"You are on the west southern section of a looping road. To the east is Cook Gate and to the west is Cook Crescent.",
npclist,
"Brighouse")

spires_w_cook = Room("Spires W at Cook Crescent",
["Cook Crescent W", "none", "West Spires Road S", "Spires Road SSW"],
None,
"You are at the intersection of Spires Road and Cook Crescent.",
npclist,
"Brighouse")

spires_road_ssw = Room("Spires Road SSW",
["none", "none", "Spires W at Cook Crescent", "Spires SW Corner"],
None,
"You are on the SSW section of a looping road. To the east is Cook Crescent.",
npclist,
"Brighouse")

spires_sw_corner = Room("Spires SW Corner",
["Spires Road WSW", "none", "Spires Road SSW", "none"],
None,
"You are at the SW corner of a looping road.",
npclist,
"Brighouse")

spires_road_wsw = Room("Spires Road WSW",
["Spires Gate at Spires Road", "Spires SW Corner", "none", "none"],
None,
"You are on the WSW section of a looping road. To the north is Spires Gate.",
npclist,
"Brighouse")

cook_cres_w = Room("Cook Crescent W",
["Cook Crescent W Corner", "Spires W at Cook Crescent", "none", "none"],
None,
"You are on the west section of a looping road. To the south is Spires Gate.",
npclist,
"Brighouse")

cook_w_corner = Room("Cook Crescent W Corner",
["none", "Cook Crescent W", "Cook Crescent N", "none"],
None,
"You are at the W corner of a looping road.",
npclist,
"Brighouse")

cook_cres_n = Room("Cook Crescent N",
["none", "none", "Cook Crescent E Corner", "Cook Crescent W Corner"],
None,
"You are at the north section of a looping road. There is a box here.",
["Seagull Flock"],
"Brighouse",
"🌾")

cook_e_corner = Room("Cook Crescent E Corner",
["none", "Cook Crescent E", "none", "Cook Crescent N"],
None,
"You are at the E corner of a looping road.",
npclist,
"Brighouse")

cook_cres_e = Room("Cook Crescent E",
["Cook Crescent E Corner", "Spires E at Cook Crescent", "none", "none"],
None,
"You are on the east section of a looping road. To the south is Spires Gate.",
npclist,
"Brighouse")

no_3_road_6300_block = Room("6300 Block No. 3 Road",
["Saba at No. 3", "Cook at No. 3", "Brighouse Station", "none"],
None,
"You are at the 6300 block of a central north-south road. To the north is Saba Road and to the south is Cook Road. To the east is a Canada Line station.",
npclist,
"Brighouse")

brighouse_station = Room("Brighouse Station",
["none", "none", "none", "6300 Block No. 3 Road"],
None,
"You are at the Brighouse Canada Line station. To the west is No. 3 Road.",
[],
"Brighouse")

buswell_street_6300_block = Room("6300 Block Buswell Street",
["Saba at Buswell", "Cook at Buswell", "none", "none"],
None,
"You are at the 6300 block of a north-south road. To the north is Saba Road and to the south is Cook Road.",
npclist,
"Brighouse")

cooney_road_6300_block = Room("6300 Block Cooney Road",
["Saba at Cooney", "Cook at Cooney", "none", "none"],
None,
"You are at the 6300 block of a north-south road. To the north is Saba Road and to the south is Cook Road.",
npclist,
"Brighouse")

cook_at_no_3 = Room("Cook at No. 3",
["6300 Block No. 3 Road", "6500 Block No. 3 Road", "8100 Block Cook Road", "none"],
None,
"You are at the intersection of Cook Road and No. 3 Road. There is a bus stop here for\n\n403",
[],
"Brighouse")

cook_road_8100_block = Room("8100 Block Cook Road",
["none", "none", "Cook at Buswell", "Cook at No. 3"],
None,
"You are at the 8100 block of an east-west road. To the east is Buswell Street and to the west is No. 3 Road.",
npclist,
"Brighouse")

cook_at_buswell = Room("Cook at Buswell",
["6300 Block Buswell Street", "6500 Block Buswell Street", "8300 Block Cook Road", "8100 Block Cook Road"],
None,
"You are at the intersection of Cook Road and Buswell Street.",
npclist,
"Brighouse")

cook_road_8300_block = Room("8300 Block Cook Road",
["none", "none", "Cook at Cooney", "Cook at Buswell"],
None,
"You are at the 8300 block of an east-west road. To the east is Cooney Road and to the west is Buswell Street.",
npclist,
"Brighouse")

cook_at_cooney = Room("Cook at Cooney",
["6300 Block Cooney Road", "6500 Block Cooney Road", "8400 Block Cook Road", "8300 Block Cook Road"],
None,
"You are at the intersection of Cook Road and Cooney Road.",
npclist,
"Brighouse")

cook_road_8400_block = Room("8400 Block Cook Road",
["none", "none", "Cook at Eckersley", "Cook at Cooney"],
None,
"You are at the 8400 block of an east-west road. To the east is Eckersley Road and to the west is Cooney Road.",
npclist,
"Brighouse")

cook_at_eckersley = Room("Cook at Eckersley",
["none", "6500 Block Eckersley Road", "8500 Block Cook Road", "8400 Block Cook Road"],
None,
"You are at the intersection of Cook Road and Eckersley Road.",
npclist,
"Brighouse")

cook_road_8500_block = Room("8500 Block Cook Road",
["none", "none", "Cook Road at Cook Gate", "Cook at Eckersley"],
None,
"You are at the 8500 block of an east-west road. To the east is Cook Gate and to the west is Eckersley Road.",
npclist,
"Brighouse")

cook_road_at_gate = Room("Cook Road at Cook Gate",
["Cook Gate", "none", "8600 Block Cook Road", "8500 Block Cook Road"],
None,
"You are at the intersection of Cook Road and Cook Gate.",
npclist,
"Brighouse")

cook_gate = Room("Cook Gate",
["Spires at Cook Gate", "Cook Road at Cook Gate", "none", "none"],
None,
"You are on a small north-south road. To the north is Spires Road and to the south is Cook Road.",
npclist,
"Brighouse")

cook_road_8600_block = Room("8600 Block Cook Road",
["none", "none", "Cook at Pimlico", "Cook Road at Cook Gate"],
None,
"You are at the 8600 block of an east-west road. To the east is Pimlico Way and to the west is Cook Gate.",
npclist,
"Brighouse")

cook_at_pimlico = Room("Cook at Pimlico",
["none", "Pimlico Way", "8800 Block Cook Road", "8600 Block Cook Road"],
None,
"You are at the intersection of Cook Road and Pimlico Way.",
npclist,
"Brighouse")

cook_road_8800_block = Room("8800 Block Cook Road",
["none", "none", "Cook at Garden City", "Cook at Pimlico"],
None,
"You are at the 8800 block of an east-west road. To the east is Garden City Road and to the west is Pimlico Way.",
npclist,
"Brighouse")

cook_at_garden_city = Room("Cook at Garden City",
["6300 Block Garden City Road", "6600 Block Garden City Road", "none", "8800 Block Cook Road"],
None,
"You are at the intersection of Cook Road and Garden City Road.",
npclist,
"Brighouse")

no_3_road_6500_block = Room("6500 Block No. 3 Road",
["Cook at No. 3", "Park at No. 3", "none", "YuBot Gift Shop Brighouse"],
None,
"You are at the 6500 block of a central north-south road. To the north is Cook Road and to the south is Park Road. To the west is a gift shop.",
npclist,
"Brighouse")

buswell_street_6500_block = Room("6500 Block Buswell Street",
["Cook at Buswell", "Park at Buswell", "none", "none"],
None,
"You are at the 6500 block of a north-south road. To the north is Cook Road and to the south is Park Road.",
npclist,
"Brighouse")

cooney_road_6500_block = Room("6500 Block Cooney Road",
["Cook at Cooney", "Park at Cooney", "none", "none"],
None,
"You are at the 6500 block of a north-south road. To the north is Cook Road and to the south is Park Road.",
npclist,
"Brighouse")

eckersley_road_6500_block = Room("6500 Block Eckersley Road",
["Cook at Eckersley", "Park at Eckersley", "none", "none"],
None,
"You are at the 6500 block of a north-south road. To the north is Cook Road and to the south is Park Road.",
npclist,
"Brighouse")

pimlico_way = Room("Pimlico Way",
["Cook at Pimlico", "Citation at Pimlico", "none", "none"],
None,
"You are on a short north-south road. To the north is Cook Road and to the south is Citation Drive.",
npclist,
"Brighouse")

garden_city_road_6600_block = Room("6600 Block Garden City Road",
["Cook at Garden City", "Citation at Garden City", "none", "none"],
None,
"You are at the 6600 block of a north-south road. To the north is Cook Road and to the south is Citation Drive.",
npclist,
"Brighouse")

park_at_no_3 = Room("Park at No. 3",
["6500 Block No. 3 Road", "6700 Block No. 3 Road", "8000 Block Park Road", "none"],
None,
"You are at the intersection of Park Road and No. 3 Road.",
npclist,
"Brighouse")

park_road_8000_block = Room("8000 Block Park Road",
["none", "none", "Park at Buswell", "Park at No. 3"],
None,
"You are at the 8000 block of an east-west road. To the east is Buswell Street and to the west is No. 3 Road.",
npclist,
"Brighouse")

park_at_buswell = Room("Park at Buswell",
["6500 Block Buswell Street", "6700 Block Buswell Street", "8200 Block Park Road", "8000 Block Park Road"],
None,
"You are at the intersection of Park Road and Buswell Street.",
npclist,
"Brighouse")

park_road_8200_block = Room("8200 Block Park Road",
["none", "none", "Park at Cooney", "Park at Buswell"],
None,
"You are at the 8200 block of a east-west road. To the east is Cooney Road and to the west is Buswell Street.",
npclist,
"Brighouse")

park_at_cooney = Room("Park at Cooney",
["6500 Block Cooney Road", "6700 Block Cooney Road", "none", "8200 Block Park Road"],
None,
"You are at the intersection of Park Road and Cooney Road.",
npclist,
"Brighouse")

park_at_eckersley = Room("Park at Eckersley",
["6500 Block Eckersley Road", "6700 Block Eckersley Road", "8500 Block Park Road", "none"],
None,
"You are at the intersection of Park Road and Eckersley Road.",
npclist,
"Brighouse")

park_road_8500_block = Room("8500 Block Park Road",
["William Cook Elementary", "none", "none", "Park at Eckersley"],
None,
"You are at the 8500 block of an east-west road. To the west is Eckersley Road. To the north is a school.",
npclist,
"Brighouse")

citation_at_pimlico = Room("Citation at Pimlico",
["Pimlico Way", "none", "8600 Block Citation Drive", "8500 Block Citation Drive"],
None,
"You are at the intersection of Citation Drive and Pimlico Way.",
npclist,
"Brighouse")

citation_drive_8600_block = Room("8600 Block Citation Drive",
["none", "none", "Citation at Garden City", "Citation at Pimlico"],
None,
"You are at the 8600 block of an east-west road. To the east is Garden City Road and to the west is Pimlico Way.",
npclist,
"Brighouse")

citation_at_garden_city = Room("Citation at Garden City",
["6600 Block Garden City Road", "6800 Block Garden City Road", "none", "8600 Block Citation Drive"],
None,
"You are at the intersection of Citation Drive and Garden City Road.",
npclist,
"Brighouse")

no_3_road_6700_block = Room("6700 Block No. 3 Road",
["Park at No. 3", "Anderson at No. 3", "none", "none"],
None,
"You are at the 6700 block of a central north-south road. To the north is Park Road and to the south is Anderson Road.",
npclist,
"Brighouse")

buswell_street_6700_block = Room("6700 Block Buswell Street",
["Park at Buswell", "Anderson at Buswell", "none", "none"],
None,
"You are at the 6700 block of a north-south road. To the north is Park Road and to the south is Anderson Road.",
npclist,
"Brighouse")

cooney_road_6700_block = Room("6700 Block Cooney Road",
["Park at Cooney", "Anderson at Cooney", "none", "none"],
None,
"You are at the 6700 block of a north-south road. To the north is Park Road and to the south is Anderson Road.",
npclist,
"Brighouse")

eckersley_road_6700_block = Room("6700 Block Eckersley Road",
["Park at Eckersley", "Anderson at Eckersley", "none", "none"],
None,
"You are at the 6700 block of a north-south road. To the north is Park Road and to the south is Anderson Road.",
npclist,
"Brighouse")

citation_drive_8500_block = Room("8500 Block Citation Drive",
["none", "Granville at Citation", "none", "Citation at Pimlico"],
None,
"You are at the 8500 block of a winding road. To the west is Citation Drive and to the south is Granville Avenue.",
npclist,
"Brighouse")

garden_city_6800_block = Room("6800 Block Garden City Road",
["Citation at Garden City", "Granville at Garden City", "Garden City Park", "none"],
None,
"You are at the 6800 block of a north-south road. To the north is Citation Drive and to the south is Granville Avenue. To the east is a park.",
npclist,
"Brighouse")

anderson_at_no_3 = Room("Anderson at No. 3",
["6700 Block No. 3 Road", "6900 Block No. 3 Road", "8100 Block Anderson Road", "none"],
None,
"You are at the intersection of Anderson Road and No. 3 Road.",
npclist,
"Brighouse")

anderson_road_8100_block = Room("8100 Block Anderson Road",
["none", "none", "Anderson at Buswell", "Anderson at No. 3"],
None,
"You are at the 8100 block of an east-west road. To the east is Buswell Street and to the west is No. 3 Road.",
npclist,
"Brighouse")

anderson_at_buswell = Room("Anderson at Buswell",
["6700 Block Buswell Street", "6900 Block Buswell Street",
"none", "8100 Block Anderson Road"],
None,
"You are at the intersection of Anderson Road and Buswell Street.",
npclist,
"Brighouse")

anderson_at_cooney = Room("Anderson at Cooney",
["6700 Block Cooney Road", "6900 Block Cooney Road", "8400 Block Anderson Road", "none"],
None,
"You are at the intersection of Anderson Road and Cooney Road.",
npclist,
"Brighouse")

anderson_road_8400_block = Room("8400 Block Anderson Road",
["none", "none", "Anderson at Eckersley", "Anderson at Cooney"],
None,
"You are at the 8400 block of an east-west road. To the east is Eckersley Road and to the west is Cooney Road.",
npclist,
"Brighouse")

anderson_at_eckersley = Room("Anderson at Eckersley",
["6700 Block Eckersley Road", "none", "8500 Block Anderson Road", "8400 Block Anderson Road"],
None,
"You are at the intersection of Anderson Road and Eckersley Road.",
npclist,
"Brighouse")

anderson_road_8500_block = Room("8500 Block Anderson Road",
["none", "none", "none", "Anderson at Eckersley", "none"],
None,
"You are at the 8500 block of an east-west road. To the west is Eckersley Road. There is a box here.",
["Leaf Pile"],
"Brighouse",
"🏀")

no_3_road_6900_block = Room("6900 Block No. 3 Road",
["Anderson at No. 3", "Granville at No. 3", "none", "none"],
None,
"You are at the 6900 block of a central north-south road. To the north is Anderson Road and to the south is Granville Avenue.",
npclist,
"Brighouse")

buswell_street_6900_block = Room("6900 Block Buswell Street",
["Anderson at Buswell", "Granville at Buswell", "none", "none"],
None,
"You are at the 6900 block of a north-south road. To the north is Anderson Road and to the south is Granville Avenue.",
npclist,
"Brighouse")

cooney_road_6900_block = Room("6900 Block Cooney Road",
["Anderson at Cooney", "Granville at Cooney", "none", "none"],
None,
"You are at the 6900 block of a north-south road. To the north is Anderson Road and to the south is Granville Avenue.",
npclist,
"Brighouse")

granville_at_garden_city = Room("Granville at Garden City",
["6800 Block Garden City Road", "none", "none", "8700 Block Granville Avenue"],
None,
"You are at the intersection of Granville Avenue and Garden City Road.",
npclist,
"Brighouse")

granville_avenue_8700_block = Room("8700 Block Granville Avenue",
["none", "none", "Granville at Garden City", "Granville at Citation"],
None,
"You are at the 8700 block of an east-west road. To the east is Garden City Road and to the west is Citation Drive.",
npclist,
"Brighouse")

granville_at_citation = Room("Granville at Citation",
["8500 Block Citation Drive", "none", "8700 Block Granville Avenue", "8500 Block Granville Avenue"],
None,
"You are at the intersection of Granville Avenue and Citation Drive.",
npclist,
"Brighouse")

granville_avenue_8500_block = Room("8500 Block Granville Avenue",
["none", "none", "Granville at Citation", "Granville at Cooney"],
None,
"You are at the 8500 block of an east-west road. To the east is Citation Drive and to the west is Cooney Road.",
npclist,
"Brighouse")

granville_at_cooney = Room("Granville at Cooney",
["6900 Block Cooney Road", "none", "8500 Block Granville Avenue", "8200 Block Granville Avenue"],
None,
"You are at the intersection of Granville Avenue and Cooney Road.",
npclist,
"Brighouse")

granville_avenue_8200_block = Room("8200 Block Granville Avenue",
["none", "none", "Granville at Cooney", "Granville at Buswell"],
None,
"You are at the 8200 block of an east-west road. To the east is Cooney Road and to the west is Buswell Street.",
npclist,
"Brighouse")

granville_at_buswell = Room("Granville at Buswell",
["6900 Block Buswell Street", "none", "8200 Block Granville Avenue", "8000 Block Granville Avenue"],
None,
"You are at the intersection of Granville Avenue and Buswell Street.",
npclist,
"Brighouse")

granville_avenue_8000_block = Room("8000 Block Granville Avenue",
["none", "none", "Granville at Buswell", "Granville at No. 3"],
None,
"You are at the 8000 block of an east-west road. To the east is Buswell Street and to the west is No. 3 Road.",
npclist,
"Brighouse")

granville_at_no_3 = Room("Granville at No. 3",
["6900 Block No. 3 Road", "none", "8000 Block Granville Avenue", "7800 Block Granville Avenue"],
None,
"You are at the intersection of Granville Avenue and No. 3 Road. There is a bus stop here for\n\n403",
[],
"Brighouse")

granville_avenue_7800_block = Room("7800 Block Granville Avenue",
["none", "Brighouse Park", "Granville at No. 3", "Granville at Minoru"],
None,
"You are at the 7800 block of an east-west road. To the east is No. 3 Road and to the west is Minoru Boulevard. To the south is a park.",
npclist,
"Brighouse")

granville_at_minoru = Room("Granville at Minoru",
["none", "none", "7800 Block Granville Avenue", "7700 Block Granville Avenue"],
None,
"You are at the intersection of Granville Avenue and Minoru Boulevard",
npclist,
"Brighouse")

granville_avenue_7700_block = Room("7700 Block Granville Avenue",
["none", "none", "Granville at Minoru", "Granville at Minoru Gate"],
None,
"You are at the 7700 block of an east-west road. To the east is Minoru Boulevard.",
npclist,
"Brighouse")

granville_at_minoru_gate = Room("Granville at Minoru Gate",
["Minoru Gate", "none", "7700 Block Granville Avenue", "none"],
None,
"You are at the intersection of Granville Avenue and Minoru Gate.",
npclist,
"Brighouse")

minoru_gate = Room("Minoru Gate",
["none", "Granville at Minoru Gate", "RPL Fountain", "none"],
None,
"You are on a small winding road. To the south is Granville Avenue and to the east is a fountain.",
npclist,
"Brighouse")

rpl_fountain = Room("RPL Fountain",
["Richmond Public Library Brighouse Branch", "none", "none", "Minoru Gate", "Terracotta Warrior"],
None,
"You are at a large fountain. To one side is a terracotta warrior statue. To the west is Minoru Gate and to the north is a library.",
npclist,
"Brighouse")

rpl_brighouse = Room("Richmond Public Library Brighouse Branch",
["none", "RPL Fountain", "none", "none"],
None,
"You are at the Brighouse branch of RPL. There is a fridge here.",
[],
"Brighouse")

yubot_bank_brighouse = Room("YuBot Bank Brighouse", 
["none", "none", "Westminster at No. 3", "none"], 
None, 
"You are at the Brighouse branch of the YuBot bank. To the east is No. 3 Road.", 
[], 
"Brighouse")

yubot_gift_shop_brighouse = Room("YuBot Gift Shop Brighouse", 
["none", "none", "6500 Block No. 3 Road", "none"], 
None,
"You are in a small gift shop. To the east is No. 3 Road. There is a sign here that says:\n\nAvailable for 50 coins:📣\nAvailable for 50 coins:🔦\nAvailable for 5000 coins:📇", 
[], 
"Brighouse")

rqshop_brighouse = Room("rqSHOP Brighouse",
["none", "8100 Block Ackroyd Road", "none", "none"],
None,
"You are in a small trinket shop. To the south is Ackroyd Road. There is a sign here that says:\n\nAvailable for 500000 coins:🔓\nAvailable for 1000000 coins:🛒\nAvailable for 1000000 coins:📡",
[], 
"Brighouse")

garden_city_lands = Room("Garden City Lands",
["none", "none", "none", "5500 Block Garden City Road"],
None,
"You are in a large expanse of open space. There is a box here. To the west is Garden City Road.",
["Pigeon Flock Redux"],
"Brighouse",
"🍂")

garden_city_park = Room("Garden City Park",
["none", "none", "none", "6800 Block Garden City Road"],
None,
"You are in a small park. To the west is Garden City Road. There is a box here.",
["Crow Flock Redux"],
"Brighouse",
"🍁")

lang_park = Room("Lang Park",
["none", "none", "none", "none", "Saba at Buswell"],
None,
"You are at a small park off Buswell Street. There is a box here.",
["Duck Redux"],
"Brighouse",
"🌻")

william_cook_elementary = Room("William Cook Elementary",
["none", "8500 Block Park Road", "none", "none"],
None,
"You are at an elementary school. To the south is Park Road. There is a box here.",
["Cougar"],
"Brighouse",
"⚽")

brighouse_park = Room("Brighouse Park",
["7800 Block Granville Avenue", "none", "none", "none"],
None,
"You are at a small park. There is a box here. To the north is Granville Avenue.",
["Goose"],
"Brighouse",
"🔑")

terracotta_warrior = Room("Terracotta Warrior",
["u0", "RPL Fountain", "RPL Fountain", "RPL Fountain"],
None,
"You moved the terracotta warrior statue and found an underground series of passageways. The entrance leads north. If you enter, you will not be able to leave. This is your last chance to turn back.",
npclist,
"Brighouse")




#--------------FINAL BOSS MAZE BELOW-----------------------


u0 = Room("u0",
["u1", "u31", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u1 = Room("u1",
["none", "none", "u36", "u29"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u2 = Room("u2",
["none", "none", "u3", "u1"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u3 = Room("u3",
["none", "none", "u4", "u2"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u4 = Room("u4",
["none", "u5", "none", "u3"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u5 = Room("u5",
["u4", "u35", "u6", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u6 = Room("u6",
["none", "none", "u5", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u7 = Room("u7",
["u6", "u8", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u8 = Room("u8",
["u7", "u37", "none", "u9"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u9 = Room("u9",
["none", "u10", "u8", "u34"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u10 = Room("u10",
["u9", "none", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u11 = Room("u11",
["none", "u12", "u10", "u13"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u12 = Room("u12",
["u11", "none", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u13 = Room("u13",
["none", "none", "u11", "u14"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u14 = Room("u14",
["none", "none", "u13", "u15"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u15 = Room("u15",
["none", "none", "u14", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u16 = Room("u16",
["u17", "u15", "u31", "u18"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u17 = Room("u17",
["none", "u16", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u18 = Room("u18",
["u19", "none", "u16", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u19 = Room("u19", #boss spawn
["u24", "u18", "none", "u20"],
None,
"You are in a dark tunnel.",
["Programmer"],
"Brighouse")

u20 = Room("u20",
["u22", "u21", "u19", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u21 = Room("u21",
["u20", "none", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u22 = Room("u22",
["u38", "u20", "u24", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u23 = Room("u23",
["none", "u24", "u25", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u24 = Room("u24",
["u23", "u19", "u26", "u22"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u25 = Room("u25",
["none", "u26", "u30", "u23"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u26 = Room("u26",
["u25", "u27", "none", "u24"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u27 = Room("u27",
["u26", "none", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u28 = Room("u28",
["u29", "none", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u29 = Room("u29",
["u30", "u28", "u26", "u1"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u30 = Room("u30",
["none", "u29", "none", "u25"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u31 = Room("u31",
["u0", "u32", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u32 = Room("u32",
["u34", "none", "u31", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u33 = Room("u33",
["none", "none", "none", "u0"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u34 = Room("u34",
["u35", "u32", "u9", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u35 = Room("u35",
["u36", "u34", "none", "u33"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u38 = Room("u38",
["none", "none", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u37 = Room("u37",
["none", "none", "none", "none"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

u36 = Room("u36",
["none", "u35", "none", "u1"],
None,
"You are in a dark tunnel.",
npclist,
"Brighouse")

#-----------------End of Brighouse Rooms---------------------
#-----------------END OF EPISODE 1---------------------------
