from src.game_const import SPRITE_HEIGHT, SPRITE_WIDTH
from src.game_enums import Direction, Music, Image
from src.helper import in_range
from src.actor import Actor
from pygame.transform import scale
from pygame.image import load


# forward declerations for type hinting
class GameModel:
    pass


class GameView:
    pass


class Oil(Actor):
    img = load(f"./assets/{Image.BARREL.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(self, x: int, y: int):
        super().__init__(x, y, visible=False, direction=Direction.RIGHT)

    def do_something(self, model: GameModel, view: GameView):
        if not self.is_visible:
            if in_range(self, model.player, 4):
                self.is_visible = True
        elif in_range(self, model.player, 3):
            self.is_alive = False
            view.play_sound(Music.FOUND_OIL.value)
            model.score += 1000
