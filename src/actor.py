from src.game_enums import Direction, Images


class Actor:
    def __init__(
        self,
        visible: bool,
        x: int,
        y: int,
        image: Images,
        direction: Direction,
        depth: int,
        size: float,
    ):
        self.visible = visible
        self.x = x
        self.y = y
        self.image = image
        self.direction = direction
        self.depth = depth
        self.size = size

    def move_to(self, x: int, y: int):
        self.x = x
        self.y = y


# animation stuff is not built out
