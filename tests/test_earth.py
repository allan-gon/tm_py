from inspect import signature
from src.actor import Actor
from src.earth import Earth


def test_earth_actor_inheritance():
    assert issubclass(Earth, Actor)


def test_num_earth_instant_params():
    assert len(signature(Earth.__init__).parameters) - 1 == 2
