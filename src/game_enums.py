from pygame.mixer import Sound
from enum import Enum, auto
from pygame import init


class GameState(Enum):
    START_MENU = auto()
    PLAYING = auto()
    LOST_LIFE_MENU = auto()
    BEAT_LEVEL_MENU = auto()
    GAME_OVER = auto()


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    DOWN = auto()
    UP = auto()


class Image(Enum):
    PLAYER = ["dig1.tga", "dig3.tga", "dig3.tga", "dig4.tga"]
    PROTESTER = ["protester1.tga", "protester2.tga", "protester3.tga"]
    HARD_CORE_PROTESTER = [
        "hardcore1.tga",
        "hardcore2.tga",
        "hardcore3.tga",
        "hardcore4.tga",
    ]
    WATER_SPURT = ["water1.tga", "water2.tga", "water3.tga"]
    BOULDER = ["rock1.tga", "rock2.tga", "rock3.tga", "rock4.tga"]
    BARREL = "barrel.tga"
    EARTH = "earth.tga"
    GOLD = "gold.tga"
    SONAR = "sonar.tga"
    WATER_POOL = "waterpool.tga"


class Music(Enum):
    init()
    THEME = Sound("./assets/theme.wav")
    PROTESTER_GIVE_UP = Sound("./assets/giveup.wav")
    PLAYER_GIVE_UP = Sound("./assets/die.wav")
    PROTESTER_YELL = Sound("./assets/goaway.wav")
    PLAYER_SQUIRT = Sound("./assets/squirt.wav")
    GOT_GOODIE = Sound("./assets/woohoo.wav")
    DIG = Sound("./assets/digging.wav")
    FINISHED_LEVEL = Sound("./assets/finished.wav")
    FOUND_OIL = Sound("./assets/foundoil.wav")
    PROTESTER_ANNOYED = Sound("./assets/ouch.wav")
    PLAYER_ANNOYED = Sound("./assets/ouch.wav")
    PROTESTER_FOUND_GOLD = Sound("./assets/bribed.wav")
    SONAR = Sound("./assets/sonar.wav")
    FALLING_ROCK = Sound("./assets/rockslide.wav")


# where should I load sounds. should this happen in the Music enum?
# make sure this only happens once
