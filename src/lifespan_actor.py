from src.game_enums import Direction
from src.actor import Actor


class LifespanActor(Actor):
    def __init__(self, x: int, y: int, visible: bool, direction: Direction):
        super().__init__(x, y, visible, direction)
