# All enemies are declared here
from items import *
enemy_goblin = {
    "id": "goblin",

    "name": "Goblin",

    "description":
    """A small green figure stands before you.""",

    "health": 20,

    "maxhealth": 20,

    "weapon_damage": 2,

    "weapon_id": "fists",

    "minexperience": 2,

    "maxexperience": 5,

    "minshronkles": 1,

    "maxshronkles": 5,

    "drops": [item_tiny_healthpotion]
}

enemy_goblin_gang = {
    "id": "Goblin party",

    "name": "Goblin Party",

    "description":
    """A Party of Goblins, a noise of giggling and obnoxious little green death.""",

    "health": 30,

    "maxhealth": 30,

    "weapon_damage": 6,

    "weapon_id": "club",

    "minexperience": 10,

    "maxexperience": 15,

    "minshronkles": 3,

    "maxshronkles": 8
}


enemy_Rat = {
    "id": "large rat",

    "name": "Large Rat",

    "description":
    """A large hairy rat hisses at you.""",

    "health": 10,

    "maxhealth": 10,

    "weapon_damage": 3,

    "weapon_id": "scratch",

    "minexperience": 1,

    "maxexperience": 3,

    "minshronkles": 1,

    "maxshronkles": 3
}

enemy_gorilla = {
    "id": "scorilla",

    "name": "Scorilla",

    "description":
    """A large beast skitters into view. It is a large grey gorilla with a scorpion tail and scorpion legs.""",

    "health": 150,

    "maxhealth": 150,

    "weapon_damage": 20,

    "weapon_id": "bigfists",

    "minexperience": 90,

    "maxexperience": 110,

    "minshronkles": 20,

    "maxshronkles": 30
}

enemy_Orc = {
    "id": "Orc",

    "name": "Orc",

    "description":
    """A tusked green orc roars at you charging axe aboved his head .""",

    "health": 50,

    "maxhealth": 50,

    "weapon_damage": 13,

    "weapon_id": "Axe",

    "minexperience": 50,

    "maxexperience": 65,

    "minshronkles": 10,

    "maxshronkles": 15
}


enemy_ogre = {
    "id": "ogre",

    "name": "Ogre",

    "description":
    """A large green manlike creature stumbles forward.""",

    "health": 200,

    "maxhealth": 200,

    "weapon_damage": 20,

    "weapon_id": "bigfists",

    "minexperience": 50,

    "maxexperience": 65,

    "minshronkles": 10,

    "maxshronkles": 15
}

enemy_cursed_skull = {
    "id": "cursed skull",

    "name": "Cursed Skull",

    "description":
    """A fiery glow appears in the distance. The facelike creature throws itself towards you""",

    "health": 100,

    "maxhealth": 100,

    "weapon_damage": 10,

    "weapon_id": "fireball",

    "minexperience": 20,

    "maxexperience": 30,

    "minshronkles": 4,

    "maxshronkles": 8
}

enemy_fire_demon = {
    "id": "fire demon",

    "name": "Fire Demon",

    "description":
    """A flaming silhouette flies towards you.""",

    "health": 50,

    "maxhealth": 50,

    "weapon_damage": 10,

    "weapon_id": "fireball",

    "minexperience": 15,

    "maxexperience": 25,

    "minshronkles": 3,

    "maxshronkles": 7
}

enemy_earth_demon = {
    "id": "earth demon",

    "name": "Earth Demon",

    "description":
    """A rocky form appears.""",

    "health": 75,

    "maxhealth": 75,

    "weapon_damage": 6,

    "weapon_id": "rockthrow",

    "minexperience": 15,

    "maxexperience": 25,

    "minshronkles": 3,

    "maxshronkles": 7
}

enemy_water_demon = {
    "id": "water demon",

    "name": "Water Demon",

    "description":
    """An watery entity appears.""",

    "health": 60,

    "maxhealth": 60,

    "weapon_damage": 7,

    "weapon_id": "scaldingwater",

    "minexperience": 15,

    "maxexperience": 25,

    "minshronkles": 3,

    "maxshronkles": 7
}

enemy_slime = {
    "id": "slime",

    "name": "slime",

    "description":
    """A puddle of slime forms, it seems agressive.""",

    "health": 15,

    "maxhealth": 15,

    "weapon_damage": 5,

    "weapon_id": "acid",

    "minexperience": 5,

    "maxexperience": 10,

    "minshronkles": 2,

    "maxshronkles": 5
}

enemy_SHRONK = {
    "id": "SHRONK",

    "name": "SHRONK",

    "description":
    """THE GREATEST AND MOST POWERFUL OF OGRES.""",

    "health": 250,

    "maxhealth": 100,

    "weapon_damage": 25,

    "weapon_id": "Shronks Shronk",

    "minexperience": 500,

    "maxexperience": 750,

    "minshronkles": 1000,

    "maxshronkles": 1000000000000000
}

enemies = {
    "SHRONK": enemy_SHRONK,
    "goblin party": enemy_goblin_gang,
    "slime": enemy_slime,
    "goblin": enemy_goblin,
    "rat": enemy_Rat,
    "gorilla": enemy_gorilla,
    "Orc": enemy_Orc,
    "ogre": enemy_ogre,
    "skull": enemy_cursed_skull,
    "fire": enemy_fire_demon,
    "earth": enemy_earth_demon,
    "water": enemy_water_demon
}
