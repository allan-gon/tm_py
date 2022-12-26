from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.actor import Actor
from enum import Enum, auto
from pygame.transform import scale
from pygame.image import load


class State(Enum):
    STABLE = auto()
    WAITING = auto()
    FALLING = auto()


class Boulder(Actor):
    imgs = [load(f"./assets/{asset}") for asset in Image.BOULDER.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self, x: int, y: int):
        self.state = State.STABLE
        super().__init__(x, y, visible=True, direction=Direction.RIGHT)

    def do_something(self, *args) -> None:
        return super().do_something(*args)
