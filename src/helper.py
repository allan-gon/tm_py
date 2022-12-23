from random import sample, randint
from src.actor import Actor


def in_range(a1: Actor, a2: Actor, distance: float = 6.0) -> bool:
    return (((a2.x - a1.x) ** 2 + (a2.y - a1.y) ** 2) ** (1 / 2)) <= distance


def gen_coords(actors: list[Actor]) -> tuple[int]:
    # i dont know how i feel about this
    temp = Actor(None, None, None, None)
    valid = False
    while not valid:
        # i think x is 27 bc things are 4x4 so
        temp.x = sample({i for i in range(0, 61)} - {i for i in range(27, 34)}, 1)[0]
        # i think 4, 60 bc top left + 4x4
        temp.y = randint(4, 60)
        for actor in actors:
            if in_range(temp, actor):
                break
        else:
            valid = True
    return temp.x, temp.y


# not within 6 units of another actor
# REMEMBER: 0,0 is top left
