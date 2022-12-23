from src.game_const import *
import pygame

pygame.init()


def test_positive_window_dims():
    assert WINDOW_WIDTH > 0
    assert WINDOW_HEIGHT > 0


def test_positive_border():
    assert BORDER > 0


def test_border_is_factor_window_dims():
    # this ensures symmetry
    assert WINDOW_WIDTH / BORDER == WINDOW_WIDTH // BORDER
    assert WINDOW_HEIGHT / BORDER == WINDOW_HEIGHT // BORDER


def test_positive_sprite_dims():
    assert SPRITE_WIDTH > 0
    assert SPRITE_HEIGHT > 0


def test_sprite_dims_are_factors_of_net_window_dims():
    assert (WINDOW_WIDTH - 2 * BORDER) / SPRITE_WIDTH == (
        WINDOW_WIDTH - BORDER
    ) // SPRITE_WIDTH
    assert (WINDOW_HEIGHT - 2 * BORDER) / SPRITE_WIDTH == (
        WINDOW_HEIGHT - BORDER
    ) // SPRITE_HEIGHT


def test_valid_font():
    assert FONT in pygame.font.get_fonts()


def test_positive_font_size():
    assert FONT_SIZE > 0


def test_positive_fps_limit():
    assert FPS_LIMIT > 0
