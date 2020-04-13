# SPRQ
A WIP re-implementation of RealityQuest, from https://repl.it/@jbrightuniverse/YuBot, rebalanced for single-player

# Modes
SPRQ allows you to experience the game in one of many modes:

**RQ 1.0 Mode**
"Classic", "RQ1", or "1.0" mode attempts to emulate the beautiful buggy mess that is the 1.0 release of RealityQuest. RQ 1.0 had many bugs and features which made the game both interesting and incredibly broken. Some highlights include:
- If you are in a room with an NPC, and you manage to defeat the NPC, if you try to exit through a non-existent exit (you stay in the same room), the NPC respawns
- If you are in a room with a boss that has a delay before it starts, you can repeatedly leave and enter the room to fight multiple instances of the boss simultaneously. This is known as "battle storage."
- You can destroy powerups which are intended to be permanent, including inventory upgrades, giving you an invalid game state
- The game is incapable of handling an empty inventory and if you destroy every item in your inventory it will treat it like an item called "None"

**RQ 1.1 Mode**
"Patched", "Enhanced", or "1.1" mode attempts to make the game more fun and patch all of the bugs in RQ 1.0 without feeling like a complete overhaul. Besides fixing the bugs, the 1.1 mode also has the original set of patches I planned for SPRQ:
- The "hole" item modifies the map, adding one extra connection between two rooms.
- The "flashlight" item shows you the secret exits in a room
- The hyper-inflated economy is deflated to reasonable levels
- The long chains of backtracking are shortened, so the game is much less repetitive

**RQ 1.5 Mode**
"SP", "Remake", or "1.5" mode is a complete remake of the original RealityQuest. It plays much more like an RPG, and contains many features which are part of RQ 2.0. Added features are:
- Dynamic HP, SP (soup points), attack, and defense stats
- Dynamic boss stats
- Dynamic, less random boss AI
- Better item balance
- All required backtracking from 1.1 mode is optional

**Co-op Mode**
RQ 1.5 Mode can optionally be rebalanced for a multiplayer environment. Co-op mode also enables features such as co-op battles and trading items or money.

**Randomizer Mode**
Randomizer Mode uses the mechanics of RQ 1.5 Mode, but every exit is randomized, every item is randomized, and you are under a strict time limit, which defautls to 1 hour. Randomizer Mode cannot save any data, so exiting ends the randomizer no matter how much time you have left. Your goal is to collect as much money and beat as many bosses as you can. A total score is calculated at the end to compare different runs.

RQ 1.5 Mode is the way I designed the game to be played. 1.0 mode and 1.1 mode may have bugs. Switching between modes deletes all save data.