from enemies import *
from items import *
from story import *

## All rooms are declared here

## Set story to 'None' without square brackets if no story is printed for that room.

room_1_a = {
    "id": "1a",

    "room": 0,

    "name": "Room Of Despair",

    "description":

    """A dark and dreary room, with very little light. A goblin's dead body lays on the floor beside with blood covering the floor around it
All you can sense is the rancid smell of rotting flesh.""",

    "exits": {"south": "Dungeonb"},

    "items": [],
    
    "enemies": [enemy_Rat],

    "possibleenemies": [enemy_Rat],

    "info": 1,

    "story": story1,

}

room_1_b = {
    "id": "1b",

    "room": 1,

    "name": "Goblin Nest",

    "description":
    """The holes in the ground seem like the goblins sleeping grounds, you notice a skeleton with a rusty sword in its rib cage.""",

    "exits": {"north": "Start", "east": "Dungeonc", "west": "Dungeond", "south": "Dungeonr"},

    "items": [item_knife],

    "enemies": [enemy_goblin_gang],

    "possibleenemies": [enemy_goblin],

    "info": 1,

    "story": story2,

}

room_1_c = {
    "id": "1c",

    "room": 2,

    "name": "Sewers",

    "description":
    """The room is covered in slime you find it hard to grasp the floor with your feet, you look at a sign on the 
wall it says septic tank don't enter without proper equipment.""",

    "exits": {"east": "Dungeont", "west": "Dungeonb"},

    "items": [item_medium_healthpotion],

    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_slime],

    "info": 1,

    "story": story3,

}
room_1_d = {
    "id": "1d",

    "room": 3,

    "name": "Greenhouse",

    "description":
    """A dark passage way with exits.""",

    "exits": {"north": "Dungeone", "east": "Dungeonb", "west": "Dungeonl"},

    "items": [],

    "enemies": [enemy_earth_demon],

    "possibleenemies": [enemy_earth_demon],

    "info": 1,

    "story": story8,

}
room_1_e = {
    "id": "1e",

    "room": 4,

    "name": "Fire Pits",

    "description":
    """A dark passage way with exits""",

    "exits": {"north": "Dungeonf", "south": "Dungeond"},

    "items": [item_tiny_healthpotion],

    "enemies": [enemy_fire_demon],

    "possibleenemies": [enemy_fire_demon],

    "info": 1,

    "story": story14,

}
room_1_f = {
    "id": "1f",

    "room": 5,

    "name": "Blacksmith",

    "description":
    """A dark passage way with exits""",

    "exits": {"east": "Dungeong", "south": "Dungeone"},

    "items": [weapon_hammer],

    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_goblin],

    "info": 1,

    "story": story17,
}
room_1_g = {
    "id": "1g",

    "room": 6,

    "name": "Burrows",

    "description":
    """A dark passage way with exits""",

    "exits": {"east": "Dungeonh", "west": "Dungeonf"},

    "items": [],
    
    "enemies": [enemy_Rat],

    "possibleenemies": [enemy_Rat, enemy_goblin],

    "info": 1,

    "story": story16,

}
room_1_h = {
    "id": "1h",

    "room": 7,

    "name": "Laboratory",

    "description":
    """A dark passage way with exits""",

    "exits": {"east": "Dungeoni", "west": "Dungeong"},

    "items": [],

    "enemies": [enemy_slime],

    "possibleenemies": [enemy_Rat, enemy_goblin, enemy_slime,],
    
    "info": 1,

    "story": story9,

}
room_1_i = {
    "id": "1i",

    "room": 8,

    "name": "Shronk's Chambers",

    "description":
    """A dark passage way with exits""",

    "exits": {"south": "Dungeonj", "west": "Dungeonh"},

    "items": [],

    "enemies": [],

    "possibleenemies": [enemy_Orc],

    "info": 1,

    "story": story4a,

}
room_1_j = {
    "id": "1j",

    "room": 9,

    "name": "Library",

    "description":
    """A dark passage way with exits""",

    "exits": {"north": "Dungeoni", "west": "Dungeonk"},

    "items": [],

    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_goblin],

    "info": 1,

    "solved": False,

    "story": story12,

}
room_1_k = {
    "id": "1k",

    "room": 10,

    "name": "Room Of Riddles",

    "description":
    """An odd looking room with a chest in the middle.""",

    "exits": {"east": "Dungeonj"},

    "items": [],
    
    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_goblin],

    "info": 1,

    "story": "",

}
room_1_l = {
    "id": "1l",

    "room": 11,

    "name": "Rock Formation",

    "description":
    """This rock outcropping has a crack in the floor from where you fought a rock elemental.""",

    "exits": {"north": "Dungeonm", "east": "Dungeond", "south": "Dungeonn"},

    "items": [],

    "enemies": [enemy_earth_demon],

    "possibleenemies": [enemy_earth_demon],

    "info": 1,

    "story": story6,

}
room_1_m = {
    "id": "1m",

    "room": 12,

    "name": "Masoluem",

    "description":
    """The room is missing skulls from the walls from where you fought them.""",

    "exits": {"south": "Dungeonl"},

    "items": [],

    "enemies": [enemy_cursed_skull],

    "possibleenemies": [enemy_cursed_skull],

    "info": 1,

    "story": story7,

}
room_1_n = {
    "id": "1n",

    "room": 13,

    "name": "Colosseum",

    "description":
    """A dark passage way with exits""",

    "exits": {"north": "Dungeonl", "east": "Dungeonq", "south": "Dungeono"},

    "items": [],

    "enemies": [enemy_cursed_skull],

    "possibleenemies": [enemy_cursed_skull],

    "info": 1,

    "story": story10,

}
room_1_o = {
    "id": "1o",

    "room": 14,

    "name": "Observatory",

    "description":
    """A dark passage way with exits""",

    "exits": {"north": "Dungeonn", "east": "Dungeonp"},

    "items": [],

    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_goblin],

    "info": 1,

    "story": story11,

}
room_1_p = {
    "id": "1p",

    "room": 15,

    "name": "Barracks",

    "description":
    """A dark passage way with exits""",

    "exits": {"north": "Dungeonq", "east": "Dungeons", "west": "Dungeono"},

    "items": [],

    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_goblin],

    "info": 1,

    "story": story20,

}
room_1_q = {
    "id": "1q",

    "room": 16,

    "name": "Dungeon",

    "description":
    """A dark passage way with exits""",

    "exits": {"east": "Dungeonr", "south": "Dungeonp", "west": "Dungeonn"},

    "items": [],

    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_goblin],

    "info": 1,

    "story": story19,

}
room_1_r = {
    "id": "1r",

    "room": 17,

    "name": "Scorilla Lair",

    "description":
    """A dark passage way with exits""",

    "exits": {"north": "Dungeonb", "west": "Dungeonq"},

    "items": [],

    "enemies": [enemy_gorilla],

    "possibleenemies": [enemy_gorilla],

    "info": 1,

    "story": "",

}
room_1_s = {
    "id": "1s",

    "room": 18,

    "name": "Royal Hall",

    "description":
    """A dark passage way with exits""",

    "exits": {"east": "Dungeonv", "west": "Dungeonp"},

    "items": [],

    "enemies": [enemy_Rat],

    "possibleenemies": [enemy_Rat],

    "info": 1,

    "story": story21,

}
room_1_t = {
    "id": "1t",

    "room": 19,

    "name": "Edge Keep",

    "description":
    """A dark passage way with exits""",

    "exits": {"south": "Dungeonu", "west": "Dungeonc"},

    "items": [],

    "enemies": [enemy_earth_demon],

    "possibleenemies": [enemy_earth_demon],

    "info": 1,

    "story": story18,

}
room_1_u = {
    "id": "1u",

    "room": 20,

    "name": "Shop",

    "description":

    """Welcome to the item shop!""",

    "exits": {"north": "Dungeont"},

    "items":  [],

    "enemies": [],

    "possibleenemies": [enemy_Rat, enemy_ogre],

    "info": 1,

    "story": story13,
}

room_1_v = {
    "id": "1v",

    "room": 21,

    "name": "Throne Room",

    "description":
    """Welcome to the throne room!""",

    "exits": {"west": "Dungeons"},

    "items": [item_magic_bean],

    "enemies": [enemy_SHRONK],

    "possibleenemies": [],

    "info": 1,

    "story": story21,

}

rooms = {
    "Start": room_1_a,
    "Dungeonb": room_1_b,
    "Dungeonc": room_1_c,
    "Dungeond": room_1_d,
    "Dungeone": room_1_e,
    "Dungeonf": room_1_f,
    "Dungeong": room_1_g,
    "Dungeonh": room_1_h,
    "Dungeoni": room_1_i,
    "Dungeonj": room_1_j,
    "Dungeonk": room_1_k,
    "Dungeonl": room_1_l,
    "Dungeonm": room_1_m,
    "Dungeonn": room_1_n,
    "Dungeono": room_1_o,
    "Dungeonp": room_1_p,
    "Dungeonq": room_1_q,
    "Dungeonr": room_1_r,
    "Dungeons": room_1_s,
    "Dungeont": room_1_t,
    "Dungeonu": room_1_u,
    "Dungeonv": room_1_v
}
