from src.game_enums import Direction


class Actor:
    # depth, size, and image are class vars since all instances will use same thing
    def __init__(self, visible: bool, x: int, y: int, direction: Direction):
        self.is_visible = visible
        self.is_alive = True
        self.x = x
        self.y = y
        self.direction = direction
        self.img_num = 0

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y
