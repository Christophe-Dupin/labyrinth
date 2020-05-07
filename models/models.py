"""[summary].

Returns:
    [type] -- [description]
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
        """Create all attribute to store date of the map.

        Arguments:
            file_name {string} -- [path to file of the map shoud be .txt]
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
        """Allow to acces to indice of the object self.list_map.

        Arguments:
            key {[int]} -- [index of item in the list]

        Returns:
            [type] -- [description]
        """
        return self.liste_map[key]

    def __contains__(self, position):
        """[summary].

        Arguments:
            position {[type]} -- [description]

        Returns:
            [Boolean] -- [if position in self.path return true]
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
        """Construct argument for hero.

        Arguments:
            map {[type]} -- [description]
            x {[int]} -- [coordinated abscisse on map]
            y {[int]} -- [coordinated ordinate on map]
        """
        self.map = map
        self.x = x
        self.y = y

    def __contains__(self, position):
        """Overload operator in for map object.

        Arguments:
            position {[tuple]} -- [coordinated x,y of hero]

        Returns:
            [Boolean] -- [return true if position in map]
        """
        return (self.x, self.y) in self.map.path

    def move(self, direction):
        """Allow to move hero in a new position which is a path.

        Arguments:
            direction {[string]} -- [which direction you want to move]
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
        """Define wich attribute is declare for an item.

        Arguments:
            position {[type]} -- [description]
            sprite {[type]} -- [description]
        """
        self.position = position
        self.sprite = sprite
        self.show = True

    def __repr__(self):
        """Allow to print an item object an return a specific string.

        Returns:
            [string] -- [return a string of the position for an item object]
        """
        return str(self.position)

    def __getitem__(self, key):
        """Allow to acces to specific element with index of item object.

        Arguments:
            key {[int]} -- [index of the element of the list]

        Returns:
            [tuple] -- [return the position]
        """
        return self.position[key]


class Lstitem:
    """Class to store multiple instances of the class Item."""

    def __init__(self, map, sprite):
        """[summary].

        Arguments:
            map {[type]} -- [description]
            sprite {[type]} -- [description]
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
        """Allow to acces to three random positions.

        Returns:
            [list] -- [return 3 random position in the map]
        """
        self.position_items = random.choices(self.map.path, k=3)
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
        """Allow to load picture and convert to pygame format.

        Arguments:
        filename {[str]} -- [path to images to convert]

        Returns:
        [pygame] -- [return the pygame object with the convert image
        to pygame format]
        """
        return pygame.image.load(filename).convert_alpha()
