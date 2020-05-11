"""Module in order to put all the data on screen with pygame."""

from config import FRAMERATE, SPRITE_SIZE

import pygame


class View:
    """Draws the model state onto the screen."""

    def __init__(self, laby, hero, sprites):
        """Instanciate all the object from models module.

        Arguments:
            map {[type]} -- [description]
            hero {[type]} -- [description]
            lstitem {[type]} -- [description]
            sprites {[type]} -- [description]
        """
        self.map = laby
        self.hero = hero
        self.sprites = sprites

    def draw(self, path, wall, vilain):

        """Allow to draw labyrinth with pygame.

        Arguments:
            path {[list]} -- [all the available path on the map]
            wall {[list]} -- [all the wall on the map]
            vilain {[list]} -- [list contrain the position of the vilain]
        """
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

        for i in self.sprites.item_list:
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

    def count_item(self):
        for i in self.sprites.item_list:
            if i.show is False:
                if self.hero.number_item == 1:
                    print("{} item found".format(self.hero.number_item))
                    break
                if self.hero.number_item >= 1:
                    print("{} items found".format(self.hero.number_item))
