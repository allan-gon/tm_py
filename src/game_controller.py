from src.game_enums import GameState, Direction, Music
from src.tunnelman import TunnelMan
from src.helper import gen_coords
from src.game_const import *
from src.earth import Earth
from src.oil import Oil
import pygame


class GameController:
    def __init__(self):
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.score = 0
        self.level = 0
        self.live = LIVES
        self.player = None
        self.earth = []
        self.barrels = []
        self.gold = []
        self.boulders = []
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
            match self.state:
                case GameState.START_MENU:
                    self.draw_start_menu()
                    if keys[pygame.K_RETURN]:
                        self.state = GameState.PLAYING
                        self.init_world()
                case GameState.PLAYING:
                    self.draw_world()
                    self.state = self.move(keys)
                case GameState.LOST_LIFE_MENU:
                    pass
                case GameState.BEAT_LEVEL_MENU:
                    pass
                case GameState.GAME_OVER:
                    # draw game over screen
                    # check if pressed enter
                    run = False
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
        self.player = TunnelMan()
        self.create_earth()
        self.calc_barrels()
        self.create_barrels()
        return

    def create_earth(self):
        self.earth = []
        for row in range(VIEW_WIDTH):
            temp = []
            for col in range(VIEW_HEIGHT):
                if row < 4:
                    temp.append(None)
                elif row > 59:
                    temp.append(Earth(col, row))
                elif 29 < col < 34:
                    temp.append(None)
                else:
                    temp.append(Earth(col, row))
            self.earth.append(temp)
        return

    def draw_actor(self, actor, image):
        # when img loaded, right is the default
        # rot is counter clock bc circle
        match actor.direction:
            case Direction.LEFT:
                image = pygame.transform.flip(image, True, False)
            case Direction.UP:
                image = pygame.transform.rotate(image, 90)
            case Direction.DOWN:
                image = pygame.transform.rotate(image, 270)
        self.window.blit(
            image,
            (
                BORDER + (actor.x * SPRITE_WIDTH * Earth.SIZE),
                BORDER + (actor.y * SPRITE_HEIGHT * Earth.SIZE),
            ),
        )
        return

    def draw_earth(self):
        for row in self.earth:
            for earth in row:
                if earth and earth.is_visible:
                    self.draw_actor(earth, Earth.img)
        return

    def draw_tm(self):
        self.draw_actor(self.player, TunnelMan.imgs[self.player.img_num])
        return

    def draw_world(self):
        # depth is just order things are drawn in
        self.draw_earth()
        self.draw_barrels()
        self.draw_tm()
        return

    def move(self, keys) -> GameState:
        self.player.do_something(keys, self.earth)

        for barrel in self.barrels:
            barrel.do_something(self)

        # i think not as innefficient as you might think. should be refs
        self.barrels = [barrel for barrel in self.barrels if barrel.is_alive]

        if not self.barrels:
            self.play_sound(Music.FINISHED_LEVEL.value)
            return GameState.BEAT_LEVEL_MENU
        elif self.player.is_alive:
            return GameState.PLAYING
        elif self.lives > 0:
            self.lives -= 1
            return GameState.LOST_LIFE_MENU
        else:
            return GameState.GAME_OVER
        return

    def play_sound(self, sound):
        sound.play()
        return

    def create_barrels(self):
        num = self.calc_barrels()
        for _ in range(num):
            dist_actors = self.barrels + self.boulders + self.gold
            x, y = gen_coords(dist_actors)
            print(x, y)
            self.barrels.append(Oil(x, y))

    def calc_barrels(self):
        return min(2 + self.level, 21)

    def draw_barrels(self):
        for barrel in self.barrels:
            if barrel.is_alive and barrel.is_visible:
                self.draw_actor(barrel, Oil.img)


# oil const needs x, y
# should that be a method or function
# if I access attributes or methods but dont change
# the class, should that be a function or method
