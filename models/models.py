"""Module in order to generate and store data for the game.

:return: [description]
:rtype: [type]
"""
import random

from config import (
    BG,
    ETHER,
    FINISH,
    FRAMERATE,
    HEIGHT,
    HERO,
    ITEM,
    NAME_WINDOW,
    PATH,
    PATH_PICTURE,
    POTION,
    START,
    VILAIN,
    WALL_PICTURE,
    WIDTH,
)

import pygame


class Map:
    """Storing data from map file map.txt."""

    def __init__(self, file_name):
        """Store an acces all datas of the map.

        :param file_name: [path of the map.txt files]
        :type file_name: [str]
        """
        self.file_name = file_name
        self.liste_map = []
        self.path = []
        self.start = []
        self.finish = []
        self.library = []
        self.wall = []
        self.parse_map()

    def __getitem__(self, key):
        """Acces to index of liste_map attribute.

        :param key: [index of the list]
        :type key: [int]
        :return: [element from the list]
        :rtype: [int]
        """
        return self.liste_map[key]

    def __contains__(self, position):
        """Overload of the operator in for Map object.

        :param position: [description]
        :type position: [tuple]
        :return: [return if position is in the liste]
        :rtype: [Boolean]
        """
        return (position.x, position.y) in self.path

    def parse_map(self):
        """Parse map.txt file to have coordinated (x,y).

        of all element of map.
        """
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
    """Storing data for Hero."""

    def __init__(self, map, x, y):
        """Init position of the hero.

        :param map: [Instance of map classe]
        :type map: [Map]
        :param x: [start position on abscisse]
        :type x: [int]
        :param y: [start position on ordered]
        :type y: [int]
        """
        self.map = map
        self.x = x
        self.y = y

    def __contains__(self, position):
        """Overload of the operator in for Hero object.

        :param position: [position to compare]
        :type position: [tuple]
        :return: [True or false]
        :rtype: [Boolean]
        """
        return (self.x, self.y) in self.map.path

    def move(self, direction):
        """Allow to stor a new position for hero if the new position is a correct path.

        :param direction: [direction you choose]
        :type direction: [str]
        """
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
    """Define what is an item object."""

    def __init__(self, position, sprite):
        """Describe what is an item.

        :param position: [position of the item]
        :type position: [tuple]
        :param sprite: [name ofthe pygame image]
        :type sprite: [pygame]
        """
        self.position = position
        self.sprite = sprite
        self.show = True

    def __repr__(self):
        """Allow to print a representation of the position.

        :return: [return the position of an item object]
        :rtype: [str]
        """
        return str(self.position)

    def __getitem__(self, key):
        """Allow to acces to index of item object.

        :param key: [index of the liste]
        :type key: [int]
        :return: [value of element of the liste]
        :rtype: [int]
        """
        return self.position[key]


class Lstitem:
    """Class to store multiple instances of the class Item."""

    def __init__(self, map, sprite):
        """Init all the item of the game.

        :param map: [instance of Map object]
        :type map: [Map]
        :param sprite: [instance of sprites object]
        :type sprite: [Sprites]
        """
        self.sprite = sprite
        self.map = map
        self.position_items = []
        self.random_items_position()
        self.item = Item(self.position_items[0], self.sprite.ether_picture)
        self.item1 = Item(self.position_items[1], self.sprite.potion_picture)
        self.item2 = Item(self.position_items[2], self.sprite.item_picture)
        self.item_list = [self.item, self.item1, self.item2]

    def random_items_position(self):
        """Allow to acces to 3 random position in the valid path of the map.

        :return: [Liste of the random position]
        :rtype: [lst]
        """
        # Create a list of start and finish coordonate
        a = self.map.start + self.map.finish
        print(a)
        # Exclude start and finish for random item position
        i = list(set(self.map.path) - (set(a)))
        print(i)
        self.position_items = random.choices(i, k=3)
        return self.position_items


class Sprites:
    """Class to initialize pygame and add methode.

    to convert images.
    """

    def __init__(self):
        """Initialize pygame module an picture object.

        for the view module.
        """
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
        self.background_picure = self.load_images(BG)

    @classmethod
    def load_images(cls, filename):
        """Class to load and convert images to pygame format.

        :param filename: [name of the file]
        :type filename: [str]
        :return: [object pygame]
        :rtype: [pygame]
        """
        return pygame.image.load(filename).convert_alpha()
