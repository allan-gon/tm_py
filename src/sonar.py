from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.actor import *
from pygame.transform import scale
from pygame.image import load


class Sonar(Actor):
    img = load(f"./assets/{Image.SONAR.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(self):
        super().__init__(0, 0, visible=True, direction=Direction.RIGHT)

    def do_something(self, *args) -> None:
        return super().do_something(*args)
