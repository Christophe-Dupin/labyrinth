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
ETHER = "data/ressource/ether.png"
POTION = "data/ressource/potion.png"
ITEM = "data/ressource/items.png"


# Window Parameter
NAME_WINDOW = "MACGAVER"
WIDTH = 300
HEIGHT = 320
SPRITE_SIZE = 20
FRAMERATE = 60
# Victory
IN_MAZE = 0
LOST = 1
WIN = 2
