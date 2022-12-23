from src.game_enums import *
from os import listdir
import pytest


@pytest.fixture
def assets():
    return listdir("./assets")


def test_valid_image_assets(assets):
    for image_file in Image:
        assert image_file.value in assets


def test_valid_sound_assets(assets):
    for audio_file in Sound:
        assert audio_file.value in assets
