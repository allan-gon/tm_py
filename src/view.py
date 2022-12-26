"""User Interface"""
from src.game_const import *
from src.game_enums import Music, Direction
from src.model import GameModel
from src.actor import Actor
from src.earth import Earth
from src.oil import Oil
from src.gold import Gold
from src.sonar import Sonar
from src.waterpool import WaterPool
from src.squirt import Squirt
from src.boulder import Boulder
from src.tunnelman import TunnelMan

# from src.protester import RegularProtester
# from src.hardcore import HardCoreProtester
from pygame.display import set_mode, set_caption, update
from pygame.transform import flip, rotate
from pygame.font import SysFont


class GameView:
    def __init__(self):
        self.window = set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.font = SysFont(FONT, FONT_SIZE)
        set_caption("TunnelMan")

    def draw_menu(self, message_1: str, message_2: str):
        m1 = self.font.render(message_1, True, "white")
        m1_rect = m1.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        m2 = self.font.render(message_2, True, "white")
        m2_rect = m2.get_rect(center=(WINDOW_WIDTH // 2, 3 * WINDOW_HEIGHT // 4))
        self.window.blit(m1, (m1_rect))
        self.window.blit(m2, (m2_rect))
        update()

    def clear_screen(self):
        self.window.fill("black")

    def draw_actor(self, actor: Actor, image):
        # when img loaded, right is the default
        # rot is counter clock bc circle
        match actor.direction:
            case Direction.LEFT:
                image = flip(image, True, False)
            case Direction.UP:
                image = rotate(image, 90)
            case Direction.DOWN:
                image = rotate(image, 270)
        self.window.blit(
            image,
            (
                BORDER + (actor.x * SPRITE_WIDTH * Earth.SIZE),
                BORDER + (actor.y * SPRITE_HEIGHT * Earth.SIZE),
            ),
        )

    def draw_earth(self, earth_container: list[list[Earth or None]]) -> None:
        for row in earth_container:
            for earth in row:
                if earth and earth.is_visible:
                    self.draw_actor(earth, Earth.img)

    def draw_actor_container(self, actor_container: list[Actor], images) -> None:
        for actor in actor_container:
            if actor.is_visible:
                if isinstance(images, list):
                    self.draw_actor(actor, images[actor.img_num])
                else:
                    self.draw_actor(actor, images)

    def draw_world(self, model: GameModel):
        self.draw_earth(model.earth)
        self.draw_actor_container(model.oil, Oil.img)
        self.draw_actor_container(model.gold, Gold.img)
        if model.sonar:
            self.draw_actor(model.sonar, Sonar.img)
        self.draw_actor_container(model.water, WaterPool.img)
        self.draw_actor_container(model.squirts, Squirt.imgs)
        self.draw_actor_container(model.boulders, Boulder.imgs)
        self.draw_actor(model.player, TunnelMan.imgs[model.player.img_num])
        # self.draw_actor_container(model.regular_protester, RegularProtester.imgs)
        # self.draw_actor_container(model.hardcore_protester, HardcoreProtester.imgs)
        update()

    def play_sound(self, sound: Music):
        sound.play()
