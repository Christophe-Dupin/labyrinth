"""Manage all the action of the game.

:return: [Victory Status]
:rtype: [Boolean]
"""
from config import LOST, WIN


class Gamemanager:
    """Mannage all the game Action."""

    def __init__(self, map, hero, view, lstitem):
        """Init all the instance of module models,view.

        :param map: [instance of class Map]
        :type map: [Map]
        :param hero: [instance of class Hero]
        :type hero: [Hero]
        :param view: [instance of class View]
        :type view: [View]
        :param lstitem: [instance of class lstitem]
        :type lstitem: [lstitem]
        """
        self.map = map
        self.hero = hero
        self.view = view
        self.lstItem = lstitem
        self.number_item = 0

    def generate_map(self):
        """Generate pygame object of the map."""
        self.view.draw(self.map.path, self.map.wall, self.map.finish)

    def get_item(self):
        """Define if the hero as the same position of one of the item."""
        for i in self.lstItem.item_list:
            if i.show is True:
                if i[0] == self.hero.x and i[1] == self.hero.y:
                    i.show = False
                    self.number_item += 1
                    print(self.number_item)

    def library(self):
        """Put item in library when hero positionand item are the same."""
        for c, i in enumerate(self.lstItem.item_list):
            if i.show is False:
                i.position = self.map.library[c]

    def victory(self):
        """Define the victory Status of the game.

        :return: [return if the user win or loose]
        :rtype: [Boolean]
        """
        for i in self.map.finish:
            if (self.hero.x, self.hero.y) == i:
                if self.number_item == len(self.lstItem.position_items):
                    return WIN
                return LOST
