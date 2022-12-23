from src.game_enums import Direction
from src.tunnelman import TunnelMan
from src.actor import Actor
from inspect import signature
import pytest


@pytest.fixture
def tm():
    return TunnelMan()


def test_num_tm_inst_params():
    assert len(signature(TunnelMan.__init__).parameters) - 1 == 0


def test_tm_actor_inheritance():
    assert issubclass(TunnelMan, Actor)


def test_tm_start_pos_dir(tm):
    assert tm.x == 30
    assert tm.y == 0
    assert tm.direction == Direction.RIGHT


def test_tm_start_pos_visual(tm):
    # TODO: pixel comparison
    assert True
