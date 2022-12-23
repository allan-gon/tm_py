from src.game_enums import Direction, Music, Image
from src.game_const import SPRITE_HEIGHT, SPRITE_WIDTH
from src.consumable import Consumable
from pygame.transform import scale
from pygame.image import load
from src.helper import in_range


class GameController:
    pass


class Oil(Consumable):
    DEPTH = 1  # check if depth is right
    img = load(f"./assets/{Image.BARREL.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(self, x: int, y: int):
        super().__init__(False, x, y, Direction.RIGHT)

    def do_something(self, gc: GameController):
        if not self.is_visible:
            if in_range(self, gc.player, 4):
                self.is_visible = True
        elif in_range(self, gc.player, 3):
            self.is_alive = False
            gc.play_sound(Music.FOUND_OIL.value)
            gc.score += 1000
