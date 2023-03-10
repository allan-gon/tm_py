# from src.entity import Entity
from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT, BORDER
from src.game_enums import Image, Direction, Music
from src.helper import boulder_obstructs
from src.actor import *
from pygame.locals import K_w, K_a, K_s, K_d, K_z, K_SPACE, K_TAB, K_ESCAPE
from pygame.transform import scale
from pygame.image import load

# class TunnelMan(Entity):
#     pass


class TunnelMan(Actor):
    imgs = [load(f"./assets/{asset}") for asset in Image.PLAYER.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self):
        self.gold_count = 0
        self.sonar_count = 1
        self.water_count = 5
        # missing health: 10
        super().__init__(30, 0, visible=True, direction=Direction.RIGHT)

    def do_something(self, model: GameModel, view: GameView, keys: list):
        # non-movement inputs
        if keys[K_ESCAPE]:
            self.is_alive = False
        elif keys[K_SPACE]:
            if self.water_count > 0:
                self.water_count -= 1
                model.try_spawn_squirt_next_to(self)
                view.play_sound(Music.PLAYER_SQUIRT)
        elif keys[K_z]:
            if self.sonar_count > 0:
                self.sonar_count -= 1
                model.use_sonar(self)
                view.play_sound(Music.SONAR)
        elif keys[K_TAB]:
            if self.gold_count > 0:
                self.gold_count -= 1
                model.place_gold(self)
        # up and down inc reversed bc origin is top left not bot left
        elif keys[K_w]:
            if self.direction == Direction.UP:
                if self.y > 0:
                    if self.dig(model.earth):
                        view.play_sound(Music.DIG)
                    if not boulder_obstructs(self, model.boulders):
                        self.y -= 1
                        self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.UP
        elif keys[K_s]:
            if self.direction == Direction.DOWN:
                if self.y < 60:
                    if self.dig(model.earth):
                        view.play_sound(Music.DIG)
                    if not boulder_obstructs(self, model.boulders):
                        self.y += 1
                        self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.DOWN
        elif keys[K_a]:
            if self.direction == Direction.LEFT:
                if self.x > 0:
                    if self.dig(model.earth):
                        view.play_sound(Music.DIG)
                    if not boulder_obstructs(self, model.boulders):
                        self.x -= 1
                        self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.LEFT
        elif keys[K_d]:
            if self.direction == Direction.RIGHT:
                if self.x < 60:
                    if self.dig(model.earth):
                        view.play_sound(Music.DIG)
                    if not boulder_obstructs(self, model.boulders):
                        self.x += 1
                        self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.RIGHT

    def dig(self, earths: list[list[Actor or None]]) -> bool:
        # digging doesn't bounds check because dig only called if in bounds
        dug = False
        match self.direction:
            case Direction.UP:
                for i in range(4):
                    earth = earths[self.y - 1][self.x + i]
                    if earth and earth.is_visible:
                        earth.is_visible = False
                        dug = True
            case Direction.DOWN:
                for i in range(4):
                    earth = earths[self.y + 4][self.x + i]
                    if earth and earth.is_visible:
                        earth.is_visible = False
                        dug = True
            case Direction.LEFT:
                for i in range(4):
                    earth = earths[self.y + i][self.x - 1]
                    if earth and earth.is_visible:
                        earth.is_visible = False
                        dug = True
            case Direction.RIGHT:
                for i in range(4):
                    earth = earths[self.y + i][self.x + 4]
                    if earth and earth.is_visible:
                        earth.is_visible = False
                        dug = True
        return dug
