import pygame
from pygame.locals import *
from models.models import Map, Item, Hero, Vilain
from view.view import View
from config import WIDTH, HEIGHT, SPRITE_SIZE, NAME_WINDOW, WIN, LOST


class Gamemanager:
    def __init__(self, map, hero, view):
        self.map = map
        self.hero = hero
        self.view = view

    def generate_map(self):
        self.view.draw(self.map.path, self.map.wall, self.map.finish)

    def victory(self):
        if self.hero.status() == WIN:
            print("c'est gagné")
        elif self.hero.status() == LOST:
            print("c'est perdu")
