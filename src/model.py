from src.game_const import VIEW_HEIGHT, VIEW_WIDTH
from src.game_const import START_LIVES
from src.game_enums import GameState, Direction
from src.helper import gen_coords, in_range
from src.tunnelman import TunnelMan
from src.waterpool import WaterPool
from src.boulder import Boulder
from src.squirt import Squirt
from src.actor import Actor
from src.sonar import Sonar
from src.earth import Earth
from src.gold import Gold
from src.oil import Oil


class GameModel:
    def __init__(self) -> None:
        # house keeping game vars
        self.state: GameState = GameState.START_MENU
        self.lives: int = START_LIVES
        self.level: int = 0
        self.score: int = 0
        # actor containers
        self.earth: list[list[Earth or None]] = None
        # maybe this should start empty
        self.boulders: list[Boulder] = []
        self.player: TunnelMan = None
        self.sonar: Sonar = None
        self.water: list[WaterPool] = []
        self.squirts: list[Squirt] = []
        self.gold: list[Gold] = []
        self.oil: list[Oil] = []

    def init_earth(self) -> None:
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

    def clear_4x4(self, x, y) -> None:
        for i in range(4):
            for j in range(4):
                if self.earth[y + j][x + i]:
                    self.earth[y + j][x + i].is_visible = False

    def calc_oil(self) -> int:
        return min(2 + self.level, 21)

    def create_oil(self) -> None:
        self.oil = []
        for _ in range(self.calc_oil()):
            dist_actors = self.oil + self.boulders + self.gold
            x, y = gen_coords(dist_actors)
            print(x, y)
            self.oil.append(Oil(x, y))

    def calc_boulders(self) -> int:
        return min((self.level // 2) + 2, 9)

    def create_boulders(self) -> None:
        self.boulders = []
        for _ in range(self.calc_boulders()):
            dist_actors = self.oil + self.boulders + self.gold
            x, y = gen_coords(dist_actors, 40)
            self.boulders.append(Boulder(x, y))
            self.clear_4x4(x, y)

    def calc_gold(self) -> int:
        return max((5 - self.level) // 2, 2)

    def create_gold(self) -> None:
        self.gold = []
        for _ in range(self.calc_gold()):
            dist_actors = self.oil + self.boulders + self.gold
            x, y = gen_coords(dist_actors)
            self.gold.append(Gold(x, y))

    def create_new_world(self) -> None:
        self.init_earth()
        self.create_oil()
        self.sonar = Sonar()
        self.create_boulders()
        self.create_gold()
        # TODO: protesters
        self.player = TunnelMan()
        print(f"Lives: {self.lives}")

    def tick(self, keys_pressed, view):
        # earth does nothing
        for oil in self.oil:
            oil.do_something(self, view)
        self.oil = [oil for oil in self.oil if oil.is_alive]

        for gold in self.gold:
            gold.do_something(self, view)
        self.gold = [gold for gold in self.gold if gold.is_alive]

        if self.sonar:
            self.sonar.do_something()
            if not self.sonar.is_alive:
                self.sonar = None

        for pool in self.water:
            pool.do_something()
        self.water = [pool for pool in self.water if pool.is_alive]

        for spurt in self.squirts:
            spurt.do_something()
        self.squirts = [spurt for spurt in self.squirts if spurt.is_alive]

        for boulder in self.boulders:
            boulder.do_something(self, view)
        self.boulders = [boulder for boulder in self.boulders if boulder.is_alive]

        self.player.do_something(keys_pressed, self.earth)

        # TODO: missing protesters

        if not self.oil:
            self.score += 1000
            self.state = GameState.BEAT_LEVEL_MENU
        elif self.player.is_alive:
            self.state = GameState.PLAYING
        elif self.lives > 0:
            self.lives -= 1
            if not self.lives:
                self.state = GameState.GAME_OVER
            else:
                self.state = GameState.LOST_LIFE_MENU


# need to keep track of:
# level, score, lives
# a count of the following should live in the TM class
# but the collection of these objects does belong here
# health, squirts, gold, oil, sonar

# Used data class before but unsing field and default
# factory is tragic

# create at end of the tick
