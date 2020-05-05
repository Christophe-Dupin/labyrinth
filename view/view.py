import pygame
import random
from models.models import Hero, Map, Item, LstItem
from config import SPRITE_SIZE, FRAMERATE
from pygame.locals import *


class View:
    """ Draws the model state onto the screen."""

    def __init__(self, map, hero, lstItem, sprites):
        self.map = map
        self.hero = hero
        self.lstItem = lstItem
        self.sprites = sprites

    def draw(self, path, wall, vilain):
        self.sprites.screen.blit(self.sprites.background_picure, (0, 0))

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
            if (self.hero.x, self.hero.y) != vilain_position:
                self.sprites.screen.blit(
                    self.sprites.vilain_picture, (y * SPRITE_SIZE, x * SPRITE_SIZE)
                )

        for i in self.lstItem.item_list:
            if i.show:
                self.sprites.screen.blit(
                    i.sprite,
                    (i.position[1] * SPRITE_SIZE, i.position[0] * SPRITE_SIZE),
                )
            else:
                self.sprites.screen.blit(
                    i.sprite,
                    (i.position[1] * SPRITE_SIZE, i.position[0] * SPRITE_SIZE),
                )

        pygame.display.flip()
        self.sprites.clock.tick(FRAMERATE)
