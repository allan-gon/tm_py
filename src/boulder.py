from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.actor import Actor
from enum import Enum, auto
from pygame.transform import scale
from pygame.image import load


class State(Enum):
    STABLE = auto()
    WAITING = auto()
    FALLING = auto()


# forward declerations for type hinting
class GameModel:
    pass


class GameView:
    pass


class Boulder(Actor):
    imgs = [load(f"./assets/{asset}") for asset in Image.BOULDER.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self, x: int, y: int):
        self.state = State.STABLE
        super().__init__(x, y, visible=True, direction=Direction.DOWN)

    def do_something(self, model: GameModel, view: GameView) -> None:
        # don't think i need to check for alive because it should only
        # be called if alive
        match self.state:
            case State.STABLE:
                # doesn't have to check if at bottom because gen coords
                if not model.dirt_in_1x4_below_actor(self):
                    self.state = State.WAITING
            case State.WAITING:
                if self.ticks_elapsed != 30:
                    self.ticks_elapsed += 1
                else:
                    self.state = State.FALLING
                    view.play_sound(Music.FALLING_ROCK)
            case State.FALLING:
                self.y += 1
                self.img_num = (self.img_num + 1) % len(Boulder.imgs)
                if model.hit_earth_or_boulder(self):
                    self.is_alive = False
                else:
                    model.hit_entity(self)
