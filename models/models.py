from config import PATH, START, FINISH, MAC
import random
from controller.eventmanager import *


class Map:
    """Storing data from map file map.txt"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.liste_map = []
        self.path = []
        self.start = []
        self.finish = []
        self.wall = []
        self.parse_map()

    def __getitem__(self, key):
        return self.liste_map[key]

    def __contains__(self, position):
        return (position.x, position.y) in self.path

    def parse_map(self):
        with open(self.file_name, "r") as f:
            for ligne in f:
                self.liste_map.append(list(ligne.strip("\n")))
            for x, ligne in enumerate(self.liste_map):
                for y, colum in enumerate(ligne):
                    if colum == PATH:
                        self.path.append((x, y))
                    elif colum == START:
                        self.start.append((x, y))
                        self.path.append((x, y))
                    elif colum == FINISH:
                        self.finish.append((x, y))
                        self.path.append((x, y))
                    else:
                        self.wall.append((x, y))


class Hero:
    """Storing data for Hero """

    def __init__(self, map, item, x, y):
        self.map = map
        self.x = x
        self.y = y
        self.item = item

    def move(self, direction):
        if direction == "moveUp":
            new_coordonne = self.x - 1, self.y
            if new_coordonne in self.map.path:
                self.x, self.y = new_coordonne

        if direction == "moveDown":
            new_coordonne = (self.x + 1, self.y)
            if new_coordonne in self.map.path:
                self.x, self.y = new_coordonne

        if direction == "moveLeft":
            new_coordonne = (self.x, self.y - 1)
            if new_coordonne in self.map.path:
                self.x, self.y = new_coordonne

        if direction == "moveRight":
            new_coordonne = (self.x, self.y + 1)
            if new_coordonne in self.map.path:
                self.x, self.y = new_coordonne


class Vilain:
    """Storing data for Vilain """

    def __init__(self, map):
        self.map = map
        self.position = self.map.finish


class Item:
    # Work in Progress
    def __init__(self, map):
        self.map = map
        self.position_items = []
        self.show = True
        self.random_items_position()

    def random_items_position(self):
        self.position_items = random.choices(self.map.path, k=3)
        return self.position_items
