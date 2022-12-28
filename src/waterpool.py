from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.helper import in_range
from src.actor import *
from pygame.transform import scale
from pygame.image import load


class WaterPool(Actor):
    img = load(f"./assets/{Image.WATER_POOL.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(self, x: int, y: int):
        super().__init__(x, y, visible=True, direction=Direction.RIGHT)

    def do_something(self, model: GameModel, view: GameView) -> None:
        if self.ticks_elapsed == model.max_tickful_actor_ticks:
            self.is_alive = False
        elif in_range(model.player, self, 3):
            self.is_alive = False
            view.play_sound(Music.GOT_GOODIE)
            model.player.water_count += 5
            model.score += 100
        self.ticks_elapsed += 1


# audio is delayed. spawning water is bugged.
# it clipped top layer
