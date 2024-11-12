# Imports items and rooms from map
from items import *
from map import rooms
from game import *



# The players stats
player_stats = {
    "maxhealth": 100,

    "health": 50,

    "level": 1,

    "experience": 0,

    "weight": 3,

    "shronkles": 0,

    "multiplier": 1
}

# Player inventory
inventory = [item_club]

# The starting room is ' '
current_room = rooms["Start"]