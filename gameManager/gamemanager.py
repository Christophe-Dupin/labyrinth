import pygame
from pygame.locals import *
from models.models import Map, Item, Hero, Vilain
from view.view import View
from config import WIDTH, HEIGHT, SPRITE_SIZE, NAME_WINDOW, WIN, LOST


class Gamemanager:
    def __init__(self, map, hero, view, lstItem):
        self.map = map
        self.hero = hero
        self.view = view
        self.lstItem = lstItem
        self.number_item = 0

    def generate_map(self):
        self.view.draw(self.map.path, self.map.wall, self.map.finish)

    def get_item(self):
        for i in self.lstItem.item_list:
            if i.show == True:
                if i[0] == self.hero.x and i[1] == self.hero.y:
                    i.show = False
                    self.number_item += 1
                    print(self.number_item)

    def victory(self):
        for i in self.map.finish:
            if (self.hero.x, self.hero.y) == i:
                if self.number_item == len(self.lstItem.position_items):
                    return WIN
                return LOST
