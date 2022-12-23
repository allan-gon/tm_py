from inspect import signature, getfullargspec
from src.game_enums import Direction
from src.actor import Actor
import pytest


def test_valid_actor_instatiation():
    assert Actor(True, 0, 0, Direction.RIGHT)


def test_actor_requires_min_4_args():
    # minus 1 because self
    assert len(signature(Actor.__init__).parameters) - 1 == 4


def test_actor_missing_arguments():
    with pytest.raises(TypeError):
        Actor()

    with pytest.raises(TypeError):
        Actor(True)

    with pytest.raises(TypeError):
        Actor(True, 0)

    with pytest.raises(TypeError):
        Actor(True, 0, 0)


def test_actor_move_to():
    actor = Actor(True, 0, 0, Direction.RIGHT)
    actor.move_to(30, 60)
    assert actor.x == 30 and actor.y == 60
