from src.game_enums import Images, Direction
from src.actor import Actor


class Earth(Actor):
    def __init__(self, x: int, y: int):
        super().__init__(True, x, y, Images.EARTH, Direction.RIGHT, 3, 0.25)
# depth is just order to draw in
