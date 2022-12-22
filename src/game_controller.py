from src.game_enums import *
from src.game_const import *
from src.earth import Earth
import pygame


class GameController:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.earth = []
        self.state = GameState.START_MENU
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("TunnelMan")
        return

    def run(self):
        pygame.font.init()
        run = True
        while run:
            # clear screen
            self.window.fill("black")
            keys = pygame.key.get_pressed()
            # draw according to state
            if self.state == GameState.START_MENU:
                self.draw_start_menu()
                if keys[pygame.K_RETURN]:
                    self.state = GameState.PLAYING
                    self.init_world()
            elif self.state == GameState.PLAYING:
                self.draw_world()
            # chek if quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            pygame.display.update()
            # follow fps limit
            self.clock.tick(FPS_LIMIT)
        pygame.quit()
        return

    def draw_start_menu(self):
        font = pygame.font.SysFont(FONT, FONT_SIZE)
        # create text and ceenter it
        welcome = font.render("Welcome to TunnelMan!", True, "white")
        w_rect = welcome.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        enter = font.render("Press Enter to begin playing", True, "white")
        e_rect = enter.get_rect(center=(WINDOW_WIDTH // 2, 3 * WINDOW_HEIGHT // 4))
        # put on screen
        self.window.blit(welcome, (w_rect))
        self.window.blit(enter, (e_rect))
        return

    def init_world(self):
        self.earth = []
        for row in range(VIEW_WIDTH):
            temp = []
            for col in range(VIEW_HEIGHT):
                if row < 4:
                    temp.append(None)
                elif row > 59:
                    temp.append(Earth(col * SPRITE_WIDTH, row * SPRITE_HEIGHT))
                elif 29 < col < 34:
                    temp.append(None)
                else:
                    temp.append(Earth(col * SPRITE_WIDTH, row * SPRITE_HEIGHT))
            self.earth.append(temp)
        return

    def draw_earth(self):
        earth_img = pygame.image.load(f"./assets/{Images.EARTH.value}")
        earth_img = pygame.transform.scale(earth_img, (SPRITE_WIDTH, SPRITE_HEIGHT))
        for row in self.earth:
            for earth in row:
                if earth and earth.is_visible:
                    self.window.blit(earth_img, (earth.x, earth.y))
        return

    def draw_tm(self):
        return

    def draw_world(self):
        self.draw_earth()
        self.draw_tm()
        return
