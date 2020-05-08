# SPRQ
SPRQ is a WIP re-implementation of RealityQuest, from https://repl.it/@jbrightuniverse/YuBot, rebalanced for single-player

![Editor Screenshot](https://raw.githubusercontent.com/Kieran-Weaver/SPRQ/master/EditorScreenshot.png)
The SPRQ Editor

# What is RealityQuest?
RealityQuest, from [the original developer's website](https://brightuniverse.weebly.com/realityquest.html), is "a multiplayer text-based adventure game," which takes place in a map based off of Metro Vancouver. It's inspired by the game *Adventure*, which was originally released in 1977 on the PDP-10 by Will Crowther and Don Woods.
The reference implementation of RealityQuest is playable on Discord, and focuses on backtracking for long chains of items to find the correct weakness for a boss.

# How to Play SPRQ
There are three ways to play SPRQ:
- Directly from the terminal, by running `python3 main.py`,
- Through Discord, by setting the environment variable TOKEN to your bot token and running `python3 spbot.py`, and
- Using the editor: Either by running `python3 editor.py` or using the prepackaged files in speditor.zip.

## Commands
Like other text-based adventure games and RPGs, you play SPRQ by entering commands.

### Movement
| Syntax                     | Description              |
|----------------------------|--------------------------|
|`w` or `west`               | Move west                |
|`n` or `north`              | Move north               |
|`e` or `east`               | Move east                |
|`s` or `south`              | Move south               |
|The name of an adjacent room| Move to that room        |
|`ride <fast-travel line>`   | Move to fast-travel room | 

You can see the names of all adjacent rooms by using the flashlight item.
You can fast-travel at any bus stop or train station. The command `ride <bus number or train line>` will transport you to the corresponding fast-travel room if you have enough money and are in the right location. From a fast-travel room, you can use the normal movement system to reach an exit.

### Combat
| Syntax                     | Description              |
|----------------------------|--------------------------|
|`attack`                    | Do basic attack          |
|`block`                     | Halve damage done to you |
|`heal`                      | Heal to full HP          |
|`use <item>`                | Use an item              |

SPRQ uses an Soup Point system to determine whether you can use `block` or `heal`. `block` costs 5 Soup Points (SP), and `heal` costs 20 SP. You start with a maximum of 10 SP, and can increase your maximum SP after leveling up. Some items restore SP.

### Items and Shops
| Syntax                     | Description                      |
|----------------------------|----------------------------------|
|`use <item>`                | Use an item                      |
|`buy <item>`                | Buy an item from the current shop|
|`sell <item>`               | Sell an item for half price      |
|`drop <item>`               | Drop item into the current room  |
|`destroy <item>`            | Delete an item permanently       |
|`get <item>`                | Get an item from the current room|

Dropping commands is not supported in Randomizer mode. In Randomizer mode, drop acts like destroy.

### Special Commands
| Syntax                     | Description                          |
|----------------------------|--------------------------------------|
|`inv` or `inventory`        | Display your inventory               |
|`profile`                   | Display your current stats           |
|`panic`                     | Die and respawn                      |
|`setmode <mode>`            | Change your game mode                |
|`levelup <stat>`            | Upgrade <stat>, using one level point|
|`open <dispenser>`          | Open the current room's dispenser    |

# Changes in SPRQ
Core Engine
- The engine is designed for purely local storage, while the reference RQ engine uses Discord channels for storage.
- The player(s) and enemies have dynamic HP, Attack, and Defense stats, making the combat much more like a traditional RPG.
- The use-soup system is replaced with the soup-point system:
	- The normal attack uses 0 soup points, and is relatively weak.
	- Stronger attacks have set soup-point values.
	- Soup restores soup points.

Boss/NPC Balance
- Items have a set damage output, which almost always ignores enemy def. Instead of necessary items, bosses now have item weaknesses.
	- No more long dependency chains in the late game.
- Rooms can be modified, allowing permanent-place holes.

Economic Balance
- The economy is significantly deflated, and more shops are region-locked.
- Bosses pay out less money every time you beat them, normal NPCs pay out relatively very little.
- In a multiplayer setting, item costs can be configured to go up over time, to compensate for renewable money sources.
- Everything gives less xp as your level goes up.

Map Changes
- When you take an exit which does not exist in a maze, you end up back at the start of the maze.
- Instead of lockers, you can store items at shops and pick them up later.

# Items
## Healing Items
| Name         | HP Healed | SP Healed | Cost | Extra effects |
|--------------|-----------|-----------|------|---------------|
| soup         | 0         | 10        | 1    | Does 2 damage |
| healthy soup | 10        | 0         | 1    | None          |
| salad        | 10        | 10        | 5    | None          |
| souper soup  | 50        | 50        | 50   | Does 1 damage |
| donut        | 50        | 50        | 20   | None          |

## Battle-specific Items
| Name        | Damage | Cost |
|-------------|--------|------|
| letter      | 3      | 5    |
| flag        | 3      | 5    |
| shield      | 3      | 5    |
| megaphone   | 4      | 8    |
| baguette    | 4      | 8    |
| script      | 4      | 8    |
| pencil      | 4      | 8    |
| cake        | 4      | 8    |
| battle soup | 5      | 10   |
| candle      | 5      | 10   |
| news        | 6      | 10   |
| snowflake   | 6      | 10   |
| leaf        | 7      | 20   |
| plant       | 7      | 20   |
| seedling    | 8      | 25   |
| flower      | 8      | 25   |
| soccer ball | 10     | 50   |
| basketball  | 10     | 50   |
| disk        | 20     | 100  |

## Powerups
| Name        | Description                                    | Cost |
|-------------|------------------------------------------------|------|
| shield      | Does 3 damage and also acts like a free `block`| 20   |
| flashlight  | Reveals hidden exits and does 5 damage         | 50   |

## Special Items
| Name        | Description                                    | Cost |
|-------------|------------------------------------------------|------|
| flashlight  | Reveals hidden exits and does 5 damage         | 50   |
| key         | Does 1 damage, but pierces defense             | 1    |

# Modes
Additionally, SPRQ allows you to experience the game in one of many modes:

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
