from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT, BORDER
from src.game_enums import Image, Direction
from src.actor import Actor

from pygame.transform import scale
from pygame.image import load


class Earth(Actor):
    DEPTH = 3
    SIZE = 0.25
    img = load(f"./assets/{Image.EARTH.value}")
    img = scale(img, (SPRITE_WIDTH * SIZE, SPRITE_HEIGHT * SIZE))

    def __init__(self, x: int, y: int):
        super().__init__(True, x, y, Direction.RIGHT)
