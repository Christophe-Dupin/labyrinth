"""Module to instanciate all the object and.

add  main loop of the game
"""
from controller.controller import Controller

from models.models import Hero, Map, Sprites

from view.view import View


class App:
    """Instanciate all objet of the game."""

    def __init__(self):
        """Instanciate all the object of the several modules."""
        self.laby = Map("data/map.txt")
        self.hero = Hero(0, 0)
        self.sprites = Sprites(self.laby.path)
        self.view = View(self.laby, self.hero, self.sprites)
        self.controller = Controller(self.hero, self.laby, self.sprites, self.view)

    def mainloop(self):
        """Loop of the game."""
        while self.controller.running:
            self.controller.process_input()
            self.controller.generate_map()


if __name__ == "__main__":
    a = App()
    a.mainloop()
