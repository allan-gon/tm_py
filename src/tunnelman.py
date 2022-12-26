# from src.entity import Entity
from src.game_const import SPRITE_WIDTH, SPRITE_HEIGHT, BORDER
from src.game_enums import Image, Direction
from src.actor import Actor
from pygame import K_w, K_a, K_s, K_d, K_SPACE, K_TAB, K_ESCAPE
from pygame.transform import scale
from pygame.image import load

# class TunnelMan(Entity):
#     pass


class TunnelMan(Actor):
    imgs = [load(f"./assets/{asset}") for asset in Image.PLAYER.value]
    imgs = [scale(img, (SPRITE_WIDTH, SPRITE_HEIGHT)) for img in imgs]

    def __init__(self):
        super().__init__(30, 0, visible=True, direction=Direction.RIGHT)

    def do_something(self, keys, earth):
        # up and down inc reversed bc origin is top left not bot left
        if keys[K_w]:
            if self.direction == Direction.UP:
                if self.y > 0:
                    self.dig(earth)
                    self.y -= 1
                    self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.UP
        elif keys[K_s]:
            if self.direction == Direction.DOWN:
                if self.y < 60:
                    self.dig(earth)
                    self.y += 1
                    self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.DOWN
        elif keys[K_a]:
            if self.direction == Direction.LEFT:
                if self.x > 0:
                    self.dig(earth)
                    self.x -= 1
                    self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.LEFT
        elif keys[K_d]:
            if self.direction == Direction.RIGHT:
                if self.x < 60:
                    self.dig(earth)
                    self.x += 1
                    self.img_num = (self.img_num + 1) % len(TunnelMan.imgs)
            else:
                self.direction = Direction.RIGHT
        return

    def dig(self, earth):
        # digging doesn't bounds check because dig only called if in bounds
        match self.direction:
            case Direction.UP:
                for i in range(4):
                    if earth[self.y - 1][self.x + i]:
                        earth[self.y - 1][self.x + i].is_visible = False
            case Direction.DOWN:
                for i in range(4):
                    if earth[self.y + 4][self.x + i]:
                        earth[self.y + 4][self.x + i].is_visible = False
            case Direction.LEFT:
                for i in range(4):
                    if earth[self.y + i][self.x - 1]:
                        earth[self.y + i][self.x - 1].is_visible = False
            case Direction.RIGHT:
                for i in range(4):
                    if earth[self.y + i][self.x + 4]:
                        earth[self.y + i][self.x + 4].is_visible = False
        return


# animate movement
# TODO: think about simpler way to check dir

# if move change image, 1, 2, 3, 4
