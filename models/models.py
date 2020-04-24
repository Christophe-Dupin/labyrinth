from config import PATH, START, FINISH, MAC
import random


class Position:
    """Class in order to return position, an update position after move """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return str((self.x, self.y))

    def __getitem__(self, key):
        return (self.x, self.y)[key]

    def __eq__(self, pos):
        return (self.x, self.y) == pos

    def moveUp(self):
        self.x = self.x - 1
        return (self.x, self.y)

    def moveDown(self):
        self.x = self.x + 1
        return (self.x, self.y)

    def moveLeft(self):
        self.y = self.y - 1
        return (self.x, self.y)

    def moveRight(self):
        self.y = self.y + 1
        return (self.x, self.y)


class Map:
    """Storing data from map file map.txt"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.liste_map = []
        self.path = []
        self.start = []
        self.finish = []
        self.wall = []

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

    def __init__(self, map):
        self.map = map
        self.position = self.map.start

    def move(self, direction):
        new_coordonne = getattr(self.position, direction)()
        if new_coordonne in self.map.path:
            self.position = new_coordonne


class Vilain:
    """Storing data for Vilain """

    def __init__(self, map):
        self.map = map
        self.position = self.map.finish


class Item:
    def __init__(self, map):
        self.map = map
        self.choosen_item = []
        self.position_items = []
        self.library = []

    def random_items_position(self):
        self.position_items = random.choices(self.map.path, k=3)
        return self.position_items
