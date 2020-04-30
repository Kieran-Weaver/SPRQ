from enum import Enum, Flag, auto
class RQMode(Enum):
	M_10 = auto()   # Pre-patch 1.0 mode
	M_11 = auto()   # Patched 1.1 mode
	M_15 = auto()   # SP mode
	M_COOP = auto() # SP Coop mode
	M_RAND = auto() # SP Randomized mode

class RQFlags(Flag):
	F_REENTER_GLITCH = auto()  # Re-entering a room retriggers the NPC (1.0 mode)
	F_BATTLE_STORAGE = auto()  # Moving during battles doesn't end the battle (1.0 mode)
	F_NECESSARY_ITEMS = auto() # NPCs can only be killed by their weaknesses (1.0 mode)
	F_BROKEN_ECONOMY = auto()  # Economy is inflated (1.0 mode), money and xp are renewable
	F_NEW_ITEMS = auto()       # Holes/Flashlights/other items have new behaviour (1.1 mode)
	F_TIMED_DAMAGE = auto()    # Damage increases over time (1.1 mode) instead of being turn-based (1.5 mode)
	F_SP_SYSTEM = auto()       # Dynamic HP/SP/ATK/DEF Stats (1.5 mode)
	F_DYNAMIC_MOVESET = auto() # Bosses have dynamic movesets (1.5 mode) instead of static attacks (1.1 mode)
	F_SEQUENCE = auto()        # You can't re-fight bosses (Possible 2.0 mode), does nothing in SP's non-linear structure
	F_DEATH_MONEY = auto()     # Money disappears on death

ModeFlags = {
	RQMode.M_10: [
		RQFlags.F_REENTER_GLITCH,
		RQFlags.F_BATTLE_STORAGE,
		RQFlags.F_NECESSARY_ITEMS,
		RQFlags.F_BROKEN_ECONOMY,
		RQFlags.F_TIMED_DAMAGE,
		RQFlags.F_DEATH_MONEY
	],
	RQMode.M_11: [
		RQFlags.F_NEW_ITEMS,
		RQFlags.F_TIMED_DAMAGE,
		RQFlags.F_DEATH_MONEY
	],
	RQMode.M_15: [
		RQFlags.F_NEW_ITEMS,
		RQFlags.F_SP_SYSTEM,
		RQFlags.F_DYNAMIC_MOVESET
	],
	RQMode.M_COOP: [
		RQFlags.F_NEW_ITEMS,
		RQFlags.F_SP_SYSTEM,
		RQFlags.F_DYNAMIC_MOVESET,
		RQFlags.F_TIMED_DAMAGE,
		RQFlags.F_DEATH_MONEY
	],
	RQMode.M_RAND: [
		RQFlags.F_NEW_ITEMS,
		RQFlags.F_SP_SYSTEM,
		RQFlags.F_DYNAMIC_MOVESET,
		RQFlags.F_SEQUENCE
	]
}

def getFlags(mode):
	if mode in ModeFlags:
		return ModeFlags[mode]
	else:
		return None
