from src.game_enums import Direction
from abc import ABC, abstractmethod


class Actor(ABC):
    # depth, size, and image are class vars since all instances will use same thing
    def __init__(self, x: int, y: int, visible: bool, direction: Direction):
        self.is_visible = visible
        self.is_alive = True
        self.x = x
        self.y = y
        self.direction = direction
        self.img_num = 0
        self.ticks_elapsed = 0

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y

    @abstractmethod
    def do_something(self, *args) -> None:
        pass


# what needs move_to?
# tm, pro, hard, bould, spurt
