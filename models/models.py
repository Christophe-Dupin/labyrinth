from config import (
    PATH,
    START,
    FINISH,
    HERO,
    VILAIN,
    WIDTH,
    HEIGHT,
    NAME_WINDOW,
    FRAMERATE,
    PATH_PICTURE,
    WALL_PICTURE,
    ETHER,
    POTION,
    ITEM,
)
import random
import pygame
from pygame.locals import *


class Map:
    """Storing data from map file map.txt"""

    def __init__(self, file_name):
        self.file_name = file_name
        self.liste_map = []
        self.path = []
        self.start = []
        self.finish = []
        self.library = []
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
                    elif colum == "$":
                        self.library.append((x, y))
                    else:
                        self.wall.append((x, y))


class Hero:
    """Storing data for Hero """

    def __init__(self, map, x, y):
        self.map = map
        self.x = x
        self.y = y

    def __contains__(self, position):
        return (self.x, self.y) in self.map.path

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


class Item:
    def __init__(self, position, sprite):
        self.position = position
        self.sprite = sprite
        self.show = True

    def __repr__(self):
        return str(self.position)

    def __getitem__(self, key):
        return self.position[key]


class LstItem:
    def __init__(self, map, sprite):
        self.sprite = sprite
        self.map = map
        self.position_items = []
        self.random_items_position()
        self.item = Item(self.position_items[0], self.sprite.ether_picture)
        self.item1 = Item(self.position_items[1], self.sprite.potion_picture)
        self.item2 = Item(self.position_items[2], self.sprite.item_picture)
        self.item_list = [self.item, self.item1, self.item2]

    def random_items_position(self):
        self.position_items = random.choices(self.map.path, k=3)
        return self.position_items


class Sprites:
    def __init__(self):
        # viewport size
        self.screen_size = WIDTH, HEIGHT

        # init pygame
        pygame.init()
        pygame.display.set_caption(NAME_WINDOW)
        self.clock = pygame.time.Clock()
        self.clock.tick(FRAMERATE)
        self.screen = pygame.display.set_mode(self.screen_size)

        # init Sprites
        self.path_picture = self.load_images(PATH_PICTURE)
        self.wall_picture = self.load_images(WALL_PICTURE)
        self.hero_picture = self.load_images(HERO)
        self.vilain_picture = self.load_images(VILAIN)
        self.ether_picture = self.load_images(ETHER)
        self.potion_picture = self.load_images(POTION)
        self.item_picture = self.load_images(ITEM)

    @classmethod
    def load_images(cls, filename):
        return pygame.image.load(filename).convert_alpha()
