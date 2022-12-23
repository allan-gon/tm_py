from src.game_enums import Direction
from src.actor import Actor


class Consumable(Actor):
    def __init__(self, visible: bool, x: int, y: int, direction: Direction):
        self.ticks_alive = 0
        super().__init__(visible, x, y, direction)
