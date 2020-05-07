<<<<<<< HEAD
from models.models import Hero, Map, Item, LstItem, Sprites
from view.view import View
from gameManager.gamemanager import Gamemanager
=======
"""Module to instanciate all the object and.

add  main loop of the game
"""
>>>>>>> develop
from controller.controller import Controller

from gameManager.gamemanager import Gamemanager

from models.models import Hero, Lstitem, Map, Sprites

from view.view import View


class App:
    """Instanciate all objet of the game."""

    def __init__(self):
        """Instanciate all the object of the several modules."""
        self.map = Map("data/map.txt")
        self.hero = Hero(self.map, 0, 0)
        self.sprites = Sprites()
        self.lstitem = Lstitem(self.map, self.sprites)
        self.view = View(self.map, self.hero, self.lstitem, self.sprites)
        self.gamemanager = Gamemanager(self.map, self.hero, self.view, self.lstitem)
        self.controller = Controller(self.gamemanager)

    def mainloop(self):
        """Loop of the game."""
        while self.controller.running:
            self.controller.process_input()
            self.gamemanager.generate_map()


if __name__ == "__main__":
    a = App()
    a.mainloop()
