from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.helper import in_range
from src.actor import *
from pygame.transform import scale
from pygame.image import load


class Sonar(Actor):
    img = load(f"./assets/{Image.SONAR.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(self):
        super().__init__(0, 0, visible=True, direction=Direction.RIGHT)

    def do_something(self, model: GameModel, view: GameView) -> None:
        if self.ticks_elapsed == model.max_tickful_actor_ticks:
            self.is_alive = False
        elif in_range(self, model.player, 3):
            self.is_alive = False
            view.play_sound(Music.GOT_GOODIE)
            model.player.sonar_count += 1
            model.score += 75
        self.ticks_elapsed += 1
