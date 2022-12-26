from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.lifespan_actor import LifespanActor
from pygame.transform import scale
from pygame.image import load


class Gold(LifespanActor):
    img = load(f"./assets/{Image.GOLD.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__(x, y, visible=False, direction=direction)

    def do_something(self, *args) -> None:
        return super().do_something(*args)
