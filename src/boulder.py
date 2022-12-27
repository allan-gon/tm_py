from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.helper import in_range
from src.actor import *
from enum import Enum, auto
from pygame.transform import scale
from pygame.image import load


class State(Enum):
    STABLE = auto()
    WAITING = auto()
    FALLING = auto()


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
                if not self.dirt_in_1x4_below_actor(model.earth):
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
                if self.hit_earth_or_boulder(model.earth, model.boulders):
                    self.is_alive = False
                else:
                    self.hit_entity(
                        model.player,  # model.regular_protesters, model.harcore_protesters
                    )

    def dirt_in_1x4_below_actor(self, earths: list[list[Actor or None]]) -> bool:
        for i in range(4):
            earth = earths[self.y + 4][self.x + i]
            if earth and earth.is_visible:
                return True
        return False

    def hit_earth_or_boulder(
        self, earth: list[list[Actor or None]], boulders: list[Actor]
    ) -> bool:
        # do i want to stop when it overlaps or the tick before
        if self.dirt_in_1x4_below_actor(earth):
            return True
        else:
            for boulder in boulders:
                # don't count yourself
                if (boulder.x != self.x) and (boulder.y != self.y):
                    if (
                        (self.x - 4) < boulder.x < (self.x + 4)
                    ) and boulder.y == self.y + 4:
                        return True
        return False

    def hit_entity(
        self,
        player: Actor,  # regular: list[Actor], hardcore: list[Actor]
    ) -> None:
        if in_range(player, self, 3):
            player.is_alive = False
            return
        # TODO: missing rg, hp, and state
        # for rp in regular:
        #     if in_range(actor, rp, 3):
        #         rp.state = State.LEAVE
        # for hp in hardcore:
        #     if in_range(actor, hp, 3):
        #         hp.state = State.LEAVE
