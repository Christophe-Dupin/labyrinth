import pygame
from pygame.locals import *
from models.models import Map, Item, Hero, Vilain
from view.view import View
from config import WIDTH, HEIGHT, SPRITE_SIZE, NAME_WINDOW


class Gamemanager:
    def __init__(self, map, hero, vilain, item, view):
        self.map = map
        self.hero = hero
        self.vilain = vilain
        self.item = item
        self.view = view
        self.generate_map()
        self.generate_hero()

        # init pygame
        pygame.init()
        pygame.display.flip()
        self.view.window(WIDTH, HEIGHT)
        self.view.window_title(NAME_WINDOW)

    def generate_map(self):
        self.view.draw_path(self.view.window(WIDTH, HEIGHT), self.map.path, SPRITE_SIZE)
        self.view.draw_wall(self.view.window(WIDTH, HEIGHT), self.map.wall, SPRITE_SIZE)
        self.view.draw_vilain(self.view.window(WIDTH, HEIGHT), SPRITE_SIZE)

    def generate_hero(self):
        self.view.draw_hero(self.view.window(WIDTH, HEIGHT), SPRITE_SIZE)
