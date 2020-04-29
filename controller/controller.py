from models.models import Hero, Vilain, Item, Map
from view.view import View
from gamemanager.gamemanager import Gamemanager
from config import WIDTH, HEIGHT, WIN, LOST
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
                elif event.key == K_RIGHT:
                    self.game_manager.hero.move("moveRight")
                elif event.key == K_UP:
                    self.game_manager.hero.move("moveUp")
                elif event.key == K_DOWN:
                    self.game_manager.hero.move("moveDown")

                if self.game_manager.hero.status() == WIN:
                    print("c'est gagné")
                elif self.game_manager.hero.status() == LOST:
                    print("c'est perdu")
