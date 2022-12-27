from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.helper import in_range
from src.actor import Actor
from pygame.transform import scale
from pygame.image import load

# forward declerations for type hinting
class GameModel:
    pass


class GameView:
    pass


class Gold(Actor):
    img = load(f"./assets/{Image.GOLD.value}")
    img = scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT))

    def __init__(
        self,
        x: int,
        y: int,
        visible: bool = False,
        placed: bool = False,
        direction: Direction = Direction.RIGHT,
    ):
        self.placed = placed
        super().__init__(x, y, visible=visible, direction=direction)

    def do_something(self, model: GameModel, view: GameView) -> None:
        # i dont think i need to check if alive because this should only be called if alive
        # if self.is_alive:
        if self.placed:
            if self.ticks_elapsed == model.tickful_actor_max_ticks:
                self.is_alive = False
            else:
                bribed = False
                for rp in model.regular_protesters:
                    if in_range(self, rp, 3):
                        self.is_alive = False
                        view.play_sound(Music.PROTESTER_FOUND_GOLD)
                        # rp.state = State.BRIBED
                        model.score += 25
                        bribed = True  # can only bribe one
                        break
                for hp in model.hardcore_protesters:
                    if in_range(self, hp, 3):
                        self.is_alive = False
                        view.play_sound(Music.PROTESTER_FOUND_GOLD)
                        # hp.state = State.BRIBED
                        model.score += 25
                        break
                self.ticks_elapsed += 1
        elif not self.is_visible:
            if in_range(self, model.player, 4):
                self.is_visible = True
        elif in_range(self, model.player, 3):
            self.is_alive = False
            view.play_sound(Music.GOT_GOODIE)
            model.score += 10
            model.player.gold += 1
