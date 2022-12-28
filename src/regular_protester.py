from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Image, Direction, Music
from src.helper import in_range, boulder_obstructs, is_clear_4x4
from src.actor import *
from pygame.transform import scale
from pygame.image import load


class RegularProtester(Actor):
    imgs = [load(f"./assets/{asset}") for asset in Image.PROTESTER.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self):
        self.health = 5
        self.state = None
        super().__init__(x=60, y=0, visible=True, direction=Direction.LEFT)

    def do_something(self, model: GameModel, view: GameView) -> None:
        pass


# i want to make sure this code works
# by spawning a single protester

# insane idea is to make a mode that goes tick by
# tick for debugging
