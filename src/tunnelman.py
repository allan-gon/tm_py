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
    DEPTH = 1  # check if depth is right
    SIZE = 1
    img = load(f"./assets/{Image.PLAYER.value}")
    img = scale(img, (SPRITE_WIDTH * SIZE, SPRITE_HEIGHT * SIZE))

    def __init__(self):
        super().__init__(True, 30, 0, Direction.RIGHT)

    def doSomething(self, keys):
        # up and down inc reversed bc origin is top left not bot left
        if keys[K_w]:
            if self.direction == Direction.UP:
                if self.y > 0:
                    self.y -= 1
            else:
                self.direction = Direction.UP
        elif keys[K_s]:
            if self.direction == Direction.DOWN:
                if self.y < 60:
                    self.y += 1
            else:
                self.direction = Direction.DOWN
        elif keys[K_a]:
            if self.direction == Direction.LEFT:
                if self.x > 0:
                    self.x -= 1
            else:
                self.direction = Direction.LEFT
        elif keys[K_d]:
            if self.direction == Direction.RIGHT:
                if self.x < 60:
                    self.x += 1
            else:
                self.direction = Direction.RIGHT

        return


# up and down dont work
