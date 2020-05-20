"""This module all aspect with user action."""
from config import LOST, WIN

import pygame
from pygame.locals import KEYDOWN, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP


class Controller:
    """Manage all the keyboard event of pygame."""

    def __init__(self, hero, laby, sprites, view):
        """Manage all of the user event from pygame.

        :param laby: [acces to Map class]
        :type laby: [MAP]
        :param hero: [acces to Hero class]
        :type hero: [Hero]
        :param sprites: [acces to sprites class]
        :type sprites: [Sprites]
        :param view: [acces to view class]
        :type view: [View]
        """
        self.running = True
        self.hero = hero
        self.laby = laby
        self.sprites = sprites
        self.view = view

    def process_input(self):
        """Manage all the keyboard event of pygame."""
        for event in pygame.event.get():
            # Pygame Event to quit or not the game
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                # Pygame event for direction of the hero
                if event.key == K_LEFT:
                    new_coordonnee = self.hero.move("moveLeft")
                elif event.key == K_RIGHT:
                    new_coordonnee = self.hero.move("moveRight")
                elif event.key == K_UP:
                    new_coordonnee = self.hero.move("moveUp")
                elif event.key == K_DOWN:
                    new_coordonnee = self.hero.move("moveDown")
                # Check if the new postion is a valid path
                if new_coordonnee in self.laby.path:
                    self.hero.x, self.hero.y = new_coordonnee
                    self.hero.bag(
                        self.sprites.item_list, self.laby.library,
                    )
                # self.view.count_item()
                # Check Victory Status
                if self.victory() == WIN:
                    self.running = False
                    print("YOU WIN")
                elif self.victory() == LOST:
                    self.running = False
                    print("YOU LOOSE")

    def generate_map(self):
        """Generate pygame object of the map."""
        self.view.draw(self.laby.path, self.laby.wall, self.laby.finish)

    def victory(self):
        """Define the victory Status of the game.

        :return: [return if the user win or loose]
        :rtype: [Boolean]
        """
        for i in self.laby.finish:
            if (self.hero.x, self.hero.y) == i:
                if self.hero.number_item == len(self.laby.library):
                    return WIN
                return LOST
