from enum import Enum


class GameState(Enum):
    START_MENU = 1
    PLAYING = 2
    LOST_LIFE_MENU = 3
    BEAT_LEVEL_MENU = 4
    GAME_OVER = 5


class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    DOWN = 3
    UP = 4


class Images(Enum):
    PLAYER = "dig1.tga"
    PROTESTER = "protester1.tga"
    HARD_CORE_PROTESTER = "hardcore1.tga"
    WATER_SPURT = "water1.tga"
    BOULDER = "rock1.tga"
    BARREL = "barrel.tga"
    EARTH = "earth.tga"
    GOLD = "gold.tga"
    SONAR = "sonar.tga"
    WATER_POOL = "waterpool.tga"
