# board and sprite dimensions
WINDOW_WIDTH = 768
WINDOW_HEIGHT = 768

VIEW_WIDTH = 64
VIEW_HEIGHT = 64

BORDER = 32

SPRITE_WIDTH = 4 * (WINDOW_WIDTH - (2 * BORDER)) // 64
SPRITE_HEIGHT = 4 * (WINDOW_HEIGHT - (2 * BORDER)) // 64

# fonts
FONT = "freeserif"
FONT_SIZE = 32

TICK_RATE = 30
FPS_LIMIT = 240
# tickrate vs fps makes no sense to me

START_LIVES = 3

# Messages to be printed on menus
START_M1 = "Welcome to TunnelMan!"
START_M2 = "Press Enter to begin playing..."
BEAT_M1 = "Woot! You finsihed the level!"
CONT = "Press Enter to continue playing..."
DIED_M1 = "You lost a life!"
OVER_M1 = "Game Over! Final score:"
OVER_M2 = "Press Enter to quit..."
