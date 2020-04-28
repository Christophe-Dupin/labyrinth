from models.models import Position, Hero, Map, Vilain, Item
from view.view import View
from gamemanager.gamemanager import Gamemanager
from controller.controller import Controller
from config import WIDTH, HEIGHT, NAME_WINDOW, SPRITE_SIZE
import pygame


if __name__ == "__main__":
    map = Map("data/map.txt")
    item = Item(map)
    hero = Hero(map, item, 0, 0)
    vilain = Vilain(map)

    view = View(map, item, hero, vilain)
    gamemanager = Gamemanager(map, hero, vilain, item, view)
    controller = Controller(gamemanager)

    while controller.running:
        controller.process_input()
        gamemanager.generate_hero()
        gamemanager.generate_map()
        tempo = pygame.time.Clock()
