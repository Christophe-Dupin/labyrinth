# -*- coding: utf-8 -*-
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent

# Constant for Terminal
START = "S"
FINISH = "F"
PATH = "."
WALL = "#"
ITEM = ["<", "^", "!", "§", "(", "%"]
MAC = "M"

# Constant Pictures
PATH_PICTURE = "data/ressource/floor.png"
WALL_PICTURE = "data/ressource/wall.png"
HERO = "data/ressource/MacGyver.png"
VILAIN = "data/ressource/Gardien.png"
BG = "data/ressources/BG.png"
ITEMS_PICTURES = [
    "data/ressource/ether.png",
    "data/ressource/potion.png",
    "data/ressource/items.png",
]

# Window Parameter
NAME_WINDOW = "MACGAVER"
WIDTH = 300
HEIGHT = 300
SPRITE_SIZE = 20
cote_fenetre = WIDTH * SPRITE_SIZE
