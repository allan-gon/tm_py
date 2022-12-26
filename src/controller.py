"""Handles interactions between Model and View"""
from src.game_enums import GameState
from src.game_const import *
from src.model import GameModel
from src.view import GameView
from pygame import init, quit, QUIT, event
from pygame.key import get_pressed
from pygame.locals import K_RETURN
from pygame.time import Clock


class GameController:
    def __init__(self):
        init()
        self.model = GameModel()
        self.view = GameView()
        self.clock = Clock()

    def run(self):
        run = True
        while run:
            # check if quit
            for e in event.get():
                if e.type == QUIT:
                    run = False
            # here the controller will tell the view what to draw
            self.view.clear_screen()
            keys_pressed = get_pressed()
            match self.model.state:
                case GameState.START_MENU:
                    self.view.draw_menu(START_M1, START_M2)
                    if keys_pressed[K_RETURN]:
                        self.model.state = GameState.PLAYING
                        self.model.create_new_world()
                case GameState.PLAYING:
                    self.view.draw_world(self.model)
                    self.model.tick(keys_pressed, self.view)
                case GameState.LOST_LIFE_MENU:
                    self.view.draw_menu(DIED_M1, CONT)
                    if keys_pressed[K_RETURN]:
                        self.model.state = GameState.PLAYING
                case GameState.BEAT_LEVEL_MENU:
                    self.view.draw_menu(BEAT_M1, CONT)
                    if keys_pressed[K_RETURN]:
                        self.model.state = GameState.PLAYING
                        self.model.create_new_world()
                case GameState.GAME_OVER:
                    self.view.draw_menu(f"{OVER_M1} {self.model.score}!", OVER_M2)
                    if keys_pressed[K_RETURN]:
                        break
            self.clock.tick(TICK_RATE)
        quit()
