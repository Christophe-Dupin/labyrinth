from models.models import Position, Hero, Vilain, Item, Map
from view.view import View


class Controller:
    def __init__(self):
        self.map = Map("data/map.txt")
        self.position = Position(0, 0)
        self.hero = Hero(self.map)
        self.vilain = Vilain(self.map)
        self.item = Item(self.map)
        self.view = View(self)

    def main(self):
        self.view.main()


if __name__ == "__main__":
    macgaver = Controller()
    macgaver.main()
