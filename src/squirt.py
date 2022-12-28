from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Direction, Image, Music
from src.helper import in_range, is_clear_4x4, boulder_obstructs
from src.actor import *
from pygame.transform import scale
from pygame.image import load


class Squirt(Actor):
    imgs = [load(f"./assets/{asset}") for asset in Image.WATER_SPURT.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self, x: int, y: int, direction: Direction):
        super().__init__(x, y, visible=True, direction=direction)

    def do_something(self, model: GameModel, view: GameView) -> None:
        if self.ticks_elapsed == 4:
            self.is_alive = False
            return
        # if squirted to death you get 100 or 250 points
        # try to deal damage to protesters
        # for rp in model.regular_protesters:
        #     if in_range(self, rp, 3):
        #         rp.health -= 2
        #         self.is_alive = False
        # for hp in model.hardcore_protesters:
        #     if in_range(self, hp, 3):
        #         hp -= 2
        #         self.is_alive = False

        # given you aren't already dead, try to move
        if is_clear_4x4(self, model.earth):
            if boulder_obstructs(self, model.boulders):
                self.is_alive = False
            else:
                match self.direction:
                    case Direction.UP:
                        self.y -= 1
                        if self.y < 0:
                            self.is_alive = False
                    case Direction.DOWN:
                        self.y += 1
                        if self.y > 60:
                            self.is_alive = False
                    case Direction.LEFT:
                        self.x -= 1
                        if self.x < 0:
                            self.is_alive = False
                    case Direction.RIGHT:
                        self.x += 1
                        if self.x > 60:
                            self.is_alive = False
        else:
            self.is_alive = False
        self.img_num = (self.img_num + 1) % len(Squirt.imgs)
        self.ticks_elapsed += 1


# TODO:
# might be dying a bit late
