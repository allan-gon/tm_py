from src.game_const import VIEW_HEIGHT, VIEW_WIDTH
from src.game_const import START_LIVES
from src.game_enums import GameState, Direction
from src.helper import *
from src.regular_protester import RegularProtester
from src.tunnelman import TunnelMan
from src.waterpool import WaterPool
from src.boulder import Boulder
from src.squirt import Squirt
from src.actor import Actor
from src.sonar import Sonar
from src.earth import Earth
from src.gold import Gold
from src.oil import Oil
from random import randint


class GameModel:
    def __init__(self) -> None:
        # house keeping game vars
        self.state: GameState = GameState.START_MENU
        self.lives: int = START_LIVES
        self.level: int = 0
        self.score: int = 0
        self.max_tickful_actor_ticks = None
        self.chance_spawn_sw = None
        self.protester_spawn_tick_buffer = None
        self.ticks_since_protester_spawn = None
        self.protester_resting_ticks = None
        self.max_protesters = None
        self.chance_hardcore = None
        # actor containers
        self.earth: list[list[Earth or None]] = None
        self.boulders: list[Boulder] = []
        self.player: TunnelMan = None
        self.sonar: Sonar = None
        self.water: list[WaterPool] = []
        self.squirts: list[Squirt] = []
        self.gold: list[Gold] = []
        self.oil: list[Oil] = []
        self.regular_protesters: list[RegularProtester] = []
        # self.harcore_protesters: list[HardcoreProtester] = []

    def get_stats(self) -> str:
        return (
            f"Lvl: {self.level} Lives: {self.lives} Hlth: {self.player.health * 10}%"
            f" Wtr: {self.player.water_count} Gld: {self.player.gold_count}"
            f" Oil left: {len(self.oil)} Sonar: {self.player.sonar_count} Scr: {self.score}"
        )

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

    def calc_tickful_max_ticks(self) -> None:
        self.max_tickful_actor_ticks = max(100, 300 - (10 * self.level))

    def calc_chance_spawn_sw(self) -> None:
        self.chance_spawn_sw = (self.level * 25) + 300

    def calc_protester_helpers(self) -> None:
        self.protester_spawn_tick_buffer = max(25, 200 - self.level)
        self.max_protesters = min(15, int(2 + (self.level * 1.5)))
        self.chance_hardcore = min(90, (self.level * 10) + 30)
        self.protester_resting_ticks = max(0, 3 - (self.level // 4))

    def create_new_world(self) -> None:
        self.init_earth()
        self.create_oil()
        self.calc_tickful_max_ticks()
        self.calc_chance_spawn_sw()
        self.sonar = Sonar()
        self.create_boulders()
        self.create_gold()
        self.water = []
        self.squirts = []
        self.calc_protester_helpers()
        self.ticks_since_protester_spawn = 0
        self.regular_protesters = []
        # self.harcore_protesters = []
        self.add_protester(force=True)
        self.player = TunnelMan()

    def try_spawn_sonar_water(self) -> None:
        # 1 is simply the sentinel
        if randint(1, self.chance_spawn_sw) == 1:
            if randint(1, 5) == 1:
                if not self.sonar:
                    self.sonar = Sonar()
            else:
                x, y = gen_coords_earthless_4x4(self.earth)
                self.water.append(WaterPool(x, y))

    def try_spawn_squirt_next_to(self, actor: Actor) -> None:
        match actor.direction:
            case Direction.UP:
                temp = Squirt(actor.x, actor.y - 4, actor.direction)
                if temp.y >= 0:
                    if is_clear_4x4(temp, self.earth):
                        for boulder in self.boulders:
                            if in_range(boulder, temp, 3):
                                break
                        else:
                            self.squirts.append(temp)
            case Direction.DOWN:
                temp = Squirt(actor.x, actor.y + 4, actor.direction)
                if temp.y <= 60:
                    if is_clear_4x4(temp, self.earth):
                        for boulder in self.boulders:
                            if in_range(boulder, temp, 3):
                                break
                        else:
                            self.squirts.append(temp)
            case Direction.LEFT:
                temp = Squirt(actor.x - 4, actor.y, actor.direction)
                if temp.x >= 0:
                    if is_clear_4x4(temp, self.earth):
                        for boulder in self.boulders:
                            if in_range(boulder, temp, 3):
                                break
                        else:
                            self.squirts.append(temp)
            case Direction.RIGHT:
                temp = Squirt(actor.x + 4, actor.y, actor.direction)
                if temp.x <= 60:
                    if is_clear_4x4(temp, self.earth):
                        for boulder in self.boulders:
                            if in_range(boulder, temp, 3):
                                break
                        else:
                            self.squirts.append(temp)

    def use_sonar(self, actor: Actor) -> None:
        hidden_actors = self.oil + self.gold
        for ha in hidden_actors:
            if in_range(ha, actor, 12):
                ha.is_visible = True

    def place_gold(self, actor: Actor) -> None:
        self.gold.append(Gold(actor.x, actor.y, True, True))

    def add_protester(self, force: bool = False) -> None:
        # self.harcore_protesters
        if (len(self.regular_protesters) + len([])) < self.max_protesters:
            if force or (
                self.ticks_since_protester_spawn >= self.protester_spawn_tick_buffer
            ):
                self.ticks_since_protester_spawn = 0
                if randint(1, 100) <= self.chance_hardcore:
                    # self.harcore_protesters.append(HardcoreProtester())
                    pass
                else:
                    self.regular_protesters.append(
                        RegularProtester(self.protester_resting_ticks)
                    )

    def tick(self, keys_pressed, view):
        # earth does nothing
        for oil in self.oil:
            oil.do_something(self, view)
        self.oil = [oil for oil in self.oil if oil.is_alive]

        for gold in self.gold:
            gold.do_something(self, view)
        self.gold = [gold for gold in self.gold if gold.is_alive]

        if self.sonar:
            self.sonar.do_something(self, view)
            if not self.sonar.is_alive:
                self.sonar = None

        for pool in self.water:
            pool.do_something(self, view)
        self.water = [pool for pool in self.water if pool.is_alive]

        for spurt in self.squirts:
            spurt.do_something(self, view)
        self.squirts = [spurt for spurt in self.squirts if spurt.is_alive]

        for boulder in self.boulders:
            boulder.do_something(self, view)
        self.boulders = [boulder for boulder in self.boulders if boulder.is_alive]

        self.player.do_something(self, view, keys_pressed)

        # TODO: missing protesters
        for rp in self.regular_protesters:
            rp.do_something(self, view)
        self.regular_protesters = [rp for rp in self.regular_protesters if rp.is_alive]

        # try to spawn actors
        self.try_spawn_sonar_water()
        # TODO: rename to try_add
        self.add_protester()

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
