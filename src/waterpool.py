from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.actor import Actor
from pygame.transform import scale
from pygame.image import load


class WaterPool(Actor):
    img = load(f"./assets/{Image.WATER_POOL.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__(x, y, visible=True, direction=direction)

    def do_something(self, *args) -> None:
        return super().do_something(*args)
