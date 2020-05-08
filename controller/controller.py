"""This module all aspect with user action."""
from config import LOST, WIN

from gameManager.gamemanager import Gamemanager
from config import WIN, LOST
import pygame
from pygame.locals import KEYDOWN, K_DOWN, K_ESCAPE, K_LEFT, K_RIGHT, K_UP


class Controller:
    """Manage all the keyboard event of pygame."""

    def __init__(self, game_manager):
        """Manage all of the user event from pygame.

        :param game_manager: [instance of gamemanager class]
        :type game_manager: [Gamemanager]
        """
        self.game_manager = game_manager
        self.running = True

    def process_input(self):
        """Manage all the keyboard event of pygame."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                if event.key == K_LEFT:
                    self.game_manager.hero.move("moveLeft")
                    self.game_manager.get_item()
                    self.game_manager.library()
                elif event.key == K_RIGHT:
                    self.game_manager.hero.move("moveRight")
                    self.game_manager.get_item()
                    self.game_manager.library()
                elif event.key == K_UP:
                    self.game_manager.hero.move("moveUp")
                    self.game_manager.get_item()
                    self.game_manager.library()
                elif event.key == K_DOWN:
                    self.game_manager.hero.move("moveDown")
                    self.game_manager.get_item()
                    self.game_manager.library()
                if self.game_manager.victory() == WIN:
                    self.running = False
                    print("YOU WIN")
                elif self.game_manager.victory() == LOST:
                    self.running = False
                    print("YOU LOOSE")
