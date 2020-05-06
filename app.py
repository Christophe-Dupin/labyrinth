from models.models import Hero, Map, Item, LstItem, Sprites
from view.view import View
from gameManager.gamemanager import Gamemanager
from controller.controller import Controller
import pygame


class App:
    def __init__(self):
        self.map = Map("data/map.txt")
        self.hero = Hero(self.map, 0, 0)
        self.sprites = Sprites()
        self.lstItem = LstItem(self.map, self.sprites)
        self.view = View(self.map, self.hero, self.lstItem, self.sprites)
        self.gamemanager = Gamemanager(self.map, self.hero, self.view, self.lstItem)
        self.controller = Controller(self.gamemanager)

    def mainloop(self):
        while self.controller.running:
            self.controller.process_input()
            self.gamemanager.generate_map()


if __name__ == "__main__":
    a = App()
    a.mainloop()
