from src.game_const import WINDOW_HEIGHT, WINDOW_WIDTH, FPS
from src.game_enums import GameState
import pygame


class GameController:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.state = GameState.START_MENU
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("TunnelMan")

    def run(self):
        run = True
        while run:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                elif self.state == GameState.START_MENU:
                    pass
        pygame.quit()
