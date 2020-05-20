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
    NAME_WINDOW,
    NEEDLE,
    PATH,
    PATH_PICTURE,
    START,
    TUBE,
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
<<<<<<< HEAD
            for ligne in f:
                self.liste_map.append(list(ligne.strip("\n")))
        for x, ligne in enumerate(self.liste_map):
            for y, colum in enumerate(ligne):
=======
            for line in f:
                self.liste_map.append(list(line.strip("\n")))
        for x, line in enumerate(self.liste_map):
            for y, colum in enumerate(line):
>>>>>>> hotfix/guillaume_feedback
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

    def __init__(self, x, y):
        """Init position of the hero.

        :param x: [start position on abscisse]
        :type x: [int]
        :param y: [start position on ordered]
        :type y: [int]
        :param number_item: [number of item get by the hero]
        :type number_item: [int]
        """
        self.x = x
        self.y = y
        self.number_item = 0

    def __contains__(self, position):
        """Overload of the operator in for Hero object.

        :param position: [position to compare]
        :type position: [tuple]
        :return: [True or false]
        :rtype: [Boolean]
        """
        return (self.x, self.y) in self.map.path

    def move(self, direction):
        """Methode to move the hero in the game.

        :param direction: [direction you choose to go]
        :type direction: [str]
        :return: [return the new position]
        :rtype: [tuple]
        """
        if direction == "moveUp":
            return (self.x - 1, self.y)

        if direction == "moveDown":
            return (self.x + 1, self.y)

        if direction == "moveLeft":
            return (self.x, self.y - 1)

        if direction == "moveRight":
            return (self.x, self.y + 1)

    def bag(self, item, library):
        """Collect item during the game.

        :param item: [List of different item in the game]
        :type item: [Sprite]
        :param library: [List of random position of item]
        :type library: [Map]
        """
        for i in item:
            if i.show is True:
                if i[0] == self.x and i[1] == self.y:
                    i.show = False
                    self.number_item += 1
                    print("{} item found".format(self.number_item))
        for c, i in enumerate(item):
            if i.show is False:
                i.position = library[c]


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


class Sprites:
    """Class to initialize pygame and add methode.

    to convert images.
    """

    def __init__(self, path):
        """Initialize pygame module an picture object.

        for the view module.
        """
        self.path = path
        # Viewport size
        self.screen_size = WIDTH, HEIGHT

        # Init pygame
        pygame.init()
        pygame.display.set_caption(NAME_WINDOW)
        self.clock = pygame.time.Clock()
        self.clock.tick(FRAMERATE)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Init Sprites
        self.path_picture = pygame.image.load(PATH_PICTURE).convert_alpha()
        self.wall_picture = pygame.image.load(WALL_PICTURE).convert_alpha()
        self.hero_picture = pygame.image.load(HERO).convert_alpha()
        self.vilain_picture = pygame.image.load(VILAIN).convert_alpha()
        self.ether_picture = pygame.image.load(ETHER).convert_alpha()
        self.potion_picture = pygame.image.load(TUBE).convert_alpha()
        self.needle_picture = pygame.image.load(NEEDLE).convert_alpha()
        self.background_picure = pygame.image.load(BG).convert_alpha()

        # Init items position and attributes
        self.position_items = random.choices(self.path, k=3)
        self.item = Item(self.position_items[0], self.ether_picture)
        self.item1 = Item(self.position_items[1], self.potion_picture)
        self.item2 = Item(self.position_items[2], self.needle_picture)
        self.item_list = [self.item, self.item1, self.item2]
