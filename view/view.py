import pygame
import random
from models.models import Hero, Map, Vilain, Item, LstItem
from config import (
    WIDTH,
    HEIGHT,
    NAME_WINDOW,
    PATH_PICTURE,
    WALL_PICTURE,
    SPRITE_SIZE,
    HERO,
    VILAIN,
    FRAMERATE,
    LOST,
    WIN,
)
from pygame.locals import *


class View:
    """ Draws the model state onto the screen."""

    def __init__(self, map, hero, lstItem, sprites):
        self.map = map
        self.hero = hero
        self.lstItem = lstItem
        self.sprites = sprites

    def draw(self, path, wall, vilain):
        for path_position in path:
            x, y = path_position
            self.sprites.screen.blit(
                self.sprites.path_picture, (y * SPRITE_SIZE, x * SPRITE_SIZE)
            )

        for wall_position in wall:
            x, y = wall_position
            self.sprites.screen.blit(
                self.sprites.wall_picture, (y * SPRITE_SIZE, x * SPRITE_SIZE)
            )

            self.sprites.screen.blit(
                self.sprites.hero_picture,
                ((self.hero.y * SPRITE_SIZE, self.hero.x * SPRITE_SIZE)),
            )
        for vilain_position in vilain:
            x, y = vilain_position
            if self.hero.status() != WIN:
                self.sprites.screen.blit(
                    self.sprites.vilain_picture, (y * SPRITE_SIZE, x * SPRITE_SIZE)
                )

        for i in self.lstItem.item_list:
            if i.show:
                self.sprites.screen.blit(
                    self.sprites.ether_picture, (i[1] * SPRITE_SIZE, i[0] * SPRITE_SIZE)
                )
                self.sprites.screen.blit(
                    self.sprites.potion_picture,
                    (i[1] * SPRITE_SIZE, i[0] * SPRITE_SIZE),
                )
                self.sprites.screen.blit(
                    self.sprites.potion_picture,
                    (i[1] * SPRITE_SIZE, i[0] * SPRITE_SIZE),
                )

        pygame.display.flip()
        self.sprites.clock.tick(FRAMERATE)
