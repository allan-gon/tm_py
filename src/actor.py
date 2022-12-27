from src.game_enums import Direction
from abc import ABC, abstractmethod


# forward declerations for type hinting
class GameModel:
    pass


class GameView:
    pass


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

    @abstractmethod
    def do_something(self, model: GameModel, view: GameView, *args) -> None:
        pass
