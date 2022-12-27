from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Image, Direction
from src.actor import *
from pygame.transform import scale
from pygame.image import load


class Earth(Actor):
    SIZE = 0.25
    img = load(f"./assets/{Image.EARTH.value}")
    img = scale(img, (SPRITE_WIDTH * SIZE, SPRITE_HEIGHT * SIZE))

    def __init__(self, x: int, y: int):
        super().__init__(x, y, visible=True, direction=Direction.RIGHT)

    def do_something(self, *args) -> None:
        # coupling here
        return super().do_something(*args)
