import pygame
from models.models import Map
from models.models import Item
from config import (
    WIDTH,
    HEIGHT,
    NAME_WINDOW,
    PATH_PICTURE,
    WALL_PICTURE,
    SPRITE_SIZE,
    ITEMS_PICTURES,
    HERO,
    VILAIN,
)
from pygame.locals import *


class View:
    """ Draws the model state onto the screen."""

    def __init__(self, map, item, hero, vilain):
        self.map = map
        self.item = item
        self.hero = hero
        self.vilain = vilain

    def window(self, width, heigh):
        a = pygame.display.set_mode((width, heigh))
        return a

    def window_title(self, name):
        pygame.display.set_caption(name)

    def draw_path(self, window, path_position, sprite_size):
        path_image = pygame.image.load(PATH_PICTURE).convert_alpha()
        for positions in path_position:
            x, y = positions
            window.blit(path_image, (y * sprite_size, x * sprite_size))

    def draw_wall(self, window, wall_position, sprite_size):
        wall_image = pygame.image.load(WALL_PICTURE).convert_alpha()
        for z in wall_position:
            x, y = z
            window.blit(wall_image, (y * sprite_size, x * sprite_size))

    def draw_hero(self, window, sprite_size):
        hero_image = pygame.image.load(HERO).convert_alpha()
        window.blit(
            hero_image, (self.hero.y * sprite_size, self.hero.x * sprite_size),
        )

    def draw_vilain(self, window, sprite_size):
        vilain_image = pygame.image.load(VILAIN).convert_alpha()
        for positions in self.vilain.position:
            x, y = positions
            window.blit(vilain_image, (y * sprite_size, x * sprite_size))
