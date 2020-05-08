"""Module in order to put all the data on screen with pygame."""

from config import FRAMERATE, SPRITE_SIZE

import pygame


class View:
    """Draws the model state onto the screen."""

    def __init__(self, map, hero, lstitem, sprites):
        """Create all the objects needed for the view.

        :param map: [instance of class Map]
        :type map: [Map]
        :param hero: [instance of class Hero]
        :type hero: [Hero]
        :param lstitem: [instance of class lstitem]
        :type lstitem: [lstitem]
        :param sprites: [instance of class Sprite]
        :type sprites: [Sprites]
        """
        self.map = map
        self.hero = hero
        self.lstItem = lstitem
        self.sprites = sprites

    def draw(self, path, wall, vilain):
        """Allow to draw the map in pygame.

        :param path: [All the coordinate path in the map]
        :type path: [list]
        :param wall: [All the coordinate wall in the map ]
        :type wall: [list]
        :param vilain: [position x,y of the vilain]
        :type vilain: [lst]
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
                    self.sprites.vilain_picture,
                    (y * SPRITE_SIZE, x * SPRITE_SIZE),
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
