from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.lifespan_actor import LifespanActor
from pygame.transform import scale
from pygame.image import load


class Squirt(LifespanActor):
    imgs = [load(f"./assets/{asset}") for asset in Image.WATER_SPURT.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__(x, y, visible=True, direction=direction)

    def do_something(self, *args) -> None:
        return super().do_something(*args)
