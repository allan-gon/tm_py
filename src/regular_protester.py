from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT
from src.game_enums import Image, Direction, Music
from src.helper import in_range, boulder_obstructs, is_clear_4x4
from src.actor import *
from pygame.transform import scale
from pygame.image import load
from enum import Enum, auto
from random import randint, choice


class State(Enum):
    REST = auto()
    LEAVE = auto()
    ACT = auto()


class RegularProtester(Actor):
    imgs = [load(f"./assets/{asset}") for asset in Image.PROTESTER.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self, resting_ticks: int):
        self.health = 5
        self.state = State.ACT
        self.resting_ticks = resting_ticks
        self.non_resting_ticks_since_shout = 0
        self.non_resting_ticks_since_perpendicular = 0
        self.num_square_move_curr_dir = randint(0, 60)
        super().__init__(x=60, y=0, visible=True, direction=Direction.LEFT)

    def do_something(self, model: GameModel, view: GameView) -> None:
        print(self.state)
        match self.state:
            case State.REST:
                if self.ticks_elapsed == self.resting_ticks:
                    self.ticks_elapsed = 0
                    self.state = State.ACT
                else:
                    self.ticks_elapsed += 1
            case State.LEAVE:
                pass
            case State.ACT:
                # regardless what you do, you must always rest following an action
                self.state = State.REST
                orthogonal = False
                # TODO: figure out facing
                if self.facing(model) and in_range(self, model.player, 4):
                    if self.non_resting_ticks_since_shout > 15:
                        print("shouting")
                        view.play_sound(Music.PROTESTER_YELL)
                        model.player.health -= 2
                        self.non_resting_ticks_since_shout = 0
                        return
                # more complicated than shares, coord.
                # straight los so nothing can obstruct
                # not sure how los is diff from 5 part c
                elif self.has_los(model) and not in_range(self, model.player, 4):
                    print("los + in range")
                    if self.y == model.player.y:
                        dir = (
                            Direction.LEFT
                            if self.x > model.player.x
                            else Direction.RIGHT
                        )
                    else:
                        dir = (
                            Direction.UP if self.y > model.player.y else Direction.DOWN
                        )
                    self.direction = dir
                    self.move(model)
                    self.img_num = (self.img_num + 1) % len(RegularProtester.imgs)
                    self.num_square_move_curr_dir = 0
                    return
                elif not self.has_los(model):
                    print("not los")
                    # TODO: fix spazing. it's close but strafes too much
                    self.num_square_move_curr_dir -= 1
                    if self.num_square_move_curr_dir < 1:
                        # pick new non-blocked dir
                        valid = False
                        dirs = [
                            Direction.UP,
                            Direction.DOWN,
                            Direction.LEFT,
                            Direction.RIGHT,
                        ]
                        while not valid:
                            dir = choice(dirs)
                            if not self.obstructed(dir, model):
                                valid = True
                        self.direction = dir
                        self.num_square_move_curr_dir = randint(8, 60)
                # # TODO: make orthogonal func
                # elif (
                #     can_move_perpedicular(self, ...)
                #     and self.non_resting_ticks_since_perpendicular > 200
                # ):
                #     # pick one that doesn't insta-block
                #     dir = ...
                #     self.direction = dir
                #     self.num_square_move_curr_dir = randint(8, 60)
                #     self.non_resting_ticks_since_perpendicular = 0
                #     orthogonal = True
                print("tried to move")
                if not self.move(model):
                    print("failed to move")
                else:
                    self.img_num = (self.img_num + 1) % len(RegularProtester.imgs)
                    self.num_square_move_curr_dir = 0
                self.non_resting_ticks_since_shout += 1
                if not orthogonal:
                    self.non_resting_ticks_since_perpendicular += 1

    def move(self, model: GameModel) -> bool:
        match self.direction:
            case Direction.UP:
                if self.obstructed(Direction.UP, model):
                    return False
                else:
                    self.y -= 1
            case Direction.DOWN:
                if self.obstructed(Direction.DOWN, model):
                    return False
                else:
                    self.y += 1
            case Direction.LEFT:
                if self.obstructed(Direction.LEFT, model):
                    return False
                else:
                    self.x -= 1
            case Direction.RIGHT:
                if self.obstructed(Direction.RIGHT, model):
                    return False
                else:
                    self.x += 1
        return True

    def facing(self, model: GameModel) -> True:
        if self.has_los(model):
            match self.direction:
                case Direction.UP:
                    return model.player.y < self.y
                case Direction.DOWN:
                    return model.player.y > self.y
                case Direction.LEFT:
                    return model.player.x < self.x
                case Direction.RIGHT:
                    return model.player.x > self.x
        return False

    def has_los(self, model: GameModel) -> bool:
        # does los mean can see all 4x4 or any?
        # because checking boulders will be more cumbersome
        if self.x == model.player.x:
            a, b = sorted([self.y, model.player.y])
            # checks if earth blocks 4x4 los
            for i in range(a, b):
                for j in range(4):
                    earth = model.earth[i][self.x + j]
                    if earth and earth.is_visible:
                        return False
            else:
                # TODO: also check against boulders
                # for boulder in model.boulders:
                #     pass
                return True
        elif self.y == model.player.y:
            a, b = sorted([self.x, model.player.x])
            for i in range(a, b):
                for j in range(4):
                    # TODO: here too
                    earth = model.earth[self.y + j][i]
                    if earth and earth.is_visible:
                        return False
            else:
                return True
        return False

    def obstructed(self, dir: Direction, model: GameModel) -> bool:
        match dir:
            case Direction.UP:
                # check earth obstructs
                for i in range(4):
                    earth = model.earth[self.y - 1][self.x + i]
                    if earth and earth.is_visible:
                        return True
                # TODO: boulder check
            case Direction.DOWN:
                # TODO: i think may go out of bounds
                for i in range(4):
                    earth = model.earth[self.y + 4][self.x + i]
                    if earth and earth.is_visible:
                        return True
            case Direction.LEFT:
                for i in range(4):
                    earth = model.earth[self.y + i][self.x - 1]
                    if earth and earth.is_visible:
                        return True
            case Direction.RIGHT:
                for i in range(4):
                    earth = model.earth[self.y + i][self.x + 4]
                    if earth and earth.is_visible:
                        return True
        return False


# insane idea is to make a mode that goes tick by
# tick for debugging
# insane progress. only mistakes were 2 or instead of
# and, and a var needed to be set each iter
