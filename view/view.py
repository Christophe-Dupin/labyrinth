import pygame
import random
from models.models import Hero, Map, Vilain, Item
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
    FRAMERATE,
    LOST,
    WIN,
)
from pygame.locals import *


class View:
    """ Draws the model state onto the screen."""

    def __init__(self, map, item, hero):
        self.map = map
        self.item = item
        self.hero = hero

        # viewport size
        self.screen_size = WIDTH, HEIGHT

        # init pygame
        pygame.init()
        pygame.display.set_caption(NAME_WINDOW)
        self.clock = pygame.time.Clock()
        self.clock.tick(FRAMERATE)
        self.screen = pygame.display.set_mode(self.screen_size)

        # convert image
        self.item_images = [
            pygame.image.load("data/ressource/ether.png").convert_alpha(),
            pygame.image.load("data/ressource/potion.png").convert_alpha(),
            pygame.image.load("data/ressource/items.png").convert_alpha(),
        ]
        self.path_image = pygame.image.load(PATH_PICTURE).convert_alpha()
        self.wall_image = pygame.image.load(WALL_PICTURE).convert_alpha()
        self.hero_image = pygame.image.load(HERO).convert_alpha()
        self.vilain_image = pygame.image.load(VILAIN).convert_alpha()

    def draw(self, path, wall, vilain):
        for path_position in path:
            x, y = path_position
            self.screen.blit(self.path_image, (y * SPRITE_SIZE, x * SPRITE_SIZE))

        for wall_position in wall:
            x, y = wall_position
            self.screen.blit(self.wall_image, (y * SPRITE_SIZE, x * SPRITE_SIZE))

            self.screen.blit(
                self.hero_image,
                ((self.hero.y * SPRITE_SIZE, self.hero.x * SPRITE_SIZE)),
            )
        for vilain_position in vilain:
            x, y = vilain_position
            if self.hero.status() != WIN:
                self.screen.blit(self.vilain_image, (y * SPRITE_SIZE, x * SPRITE_SIZE))

        for item_position in self.item.position_item:
            x, y = item_position
            if self.item.show:
                self.screen.blit(self.vilain_image, (y * SPRITE_SIZE, x * SPRITE_SIZE))

        pygame.display.flip()
        self.clock.tick(FRAMERATE)
