
from gameManager.gamemanager import Gamemanager
from config import WIN, LOST
import pygame
from pygame.locals import *


class Controller:
    def __init__(self, game_manager):
        self.game_manager = game_manager
        self.running = True

    def process_input(self):
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
                    print("c'est gagné")
                elif self.game_manager.victory() == LOST:
                    self.running = False
                    print("c'est perdu")
