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

# maybe make all params optional so 
# const here is empty and it's clear that this is garbo
# instance

# not within 6 units of another dist actor
# REMEMBER: 0,0 is top left

# You are given a 64x 64 grid
# the entire span of the top 4 rows are unavailible
# the entire span of the bottom 4 rows are availible
# the entire span center 4 columns are unavailible except for the 4 bottom rows
# An object's location is denoted by a single row, col in it's top left
# An object spans a 4x4 that is to say no object's row must be > 60 because it would go out of bounds
# Similarly no object's column must be greater than 60 and no object's col should be
# between 27 and 33 because it would intersect the shaft (unless it's at the bottom of course)
# no object can be within 6 units of euclidian distance from another object.
# Given these constraints, what is the maximum number of items a 64x64 grid can house

# max is 23 check if that checks out
# also document
# also test

# most boulders possible is 9
# most nuggets possible is 2? maybe 3
# most barrels possible is 21
# looks like the current approach of generating coords will
# break down. The safe gaurd is 33 things which
# according to chatgpt is more tahn what's availible
