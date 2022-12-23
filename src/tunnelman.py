# from src.entity import Entity
from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT, BORDER
from src.game_enums import Image, Direction
from src.actor import Actor

from pygame.transform import scale
from pygame.image import load

# class TunnelMan(Entity):
#     pass


class TunnelMan(Actor):
    DEPTH = 1  # check if depth is right
    SIZE = 1
    img = load(f"./assets/{Image.PLAYER.value}")
    img = scale(img, (SPRITE_WIDTH * SIZE, SPRITE_HEIGHT * SIZE))

    def __init__(self):
        super().__init__(True, 0, 0, Direction.RIGHT)
