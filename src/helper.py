from random import sample, randint
from src.actor import Actor
from src.earth import Earth


def in_range(a1: Actor, a2: Actor, distance: float = 6.0) -> bool:
    return (((a2.x - a1.x) ** 2 + (a2.y - a1.y) ** 2) ** (1 / 2)) <= distance


def gen_coords(actors: list[Actor], y_right: int = 60) -> tuple[int]:
    # i dont know how i feel about this
    temp = Earth(None, None)
    valid = False
    while not valid:
        # i think x is 27 bc things are 4x4 so
        temp.x = sample({i for i in range(0, 61)} - {i for i in range(27, 34)}, 1)[0]
        # i think 4, 60 bc top left + 4x4
        temp.y = randint(4, y_right)
        for actor in actors:
            if in_range(temp, actor):
                break
        else:
            valid = True
    return temp.x, temp.y


# TODO: fix
# audio is delayed. spawning water is bugged.
# it clipped top layer
def gen_coords_earthless_4x4(earths: list[list[Earth or None]]) -> tuple[int]:
    valid, broke = False, False
    while not valid:
        broke = False
        x, y = randint(0, 60), randint(0, 60)
        for i in range(4):
            for j in range(4):
                earth = earths[y + j][x + i]
                if earth and earth.is_visible:
                    broke = True
                    break
            if broke:
                break
        else:
            valid = True
    return x, y


def is_clear_4x4(actor: Actor, earths: list[list[Earth or None]]) -> bool:
    for i in range(4):
        for j in range(4):
            earth = earths[actor.y + j][actor.x + i]
            if earth and earth.is_visible:
                return False
    return True
