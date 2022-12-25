# Non-Game Objects
## Enums
- generally, I'm using enums as a more expressive way to represent certain values
- strings could suffice but I think having all the values centralized in a class is cleaner
- there's a single file `src/game_enums.py` that contains all of them
- I import Sound, init, and Enum because:
    - `pygame.mixer.Sound`: to load the sound assets and play them later
    - `pygame.init`: because Sound doesn't work if pygame is not initialized
    - `enum.Enum`: to use as the parent class

### GameState
- 5 values: START_MENU, PLAYING, LOST_LIFE_MENU, BEAT_LEVEL_MENU, and GAME_OVER
- used by GameController to figure out what should be drawn to screen

### Direction
- 4 values: LEFT, RIGHT, DOWN, and UP
- all actors have a direction, this is used to figure out how to move an actor and how to rotate the assets the actor uses

### Image
- 10 values: PLAYER, PROTESTER, HARD_CORE_PROTESTER, WATER_SPURT, BOULDER, BARREL, EARTH, GOLD, SONAR, and WATER_POOL
- this is a string or a list of strings for the asset(s) a given actor uses

### Music
- 14 values: THEME, PROTESTER_GIVE_UP, PLAYER_GIVE_UP, PROTESTER_YELL, PLAYER_SQUIRT, GOT_GOODIE, DIG, FINISHED_LEVEL, FOUND_OIL, PROTESTER_ANNOYED, PLAYER_ANNOYED, PROTESTER_FOUND_GOLD, SONAR, and FALLING_ROCK
- this is pygame Sound objects used later to play a given sound

## Constants
- the `src/game_const.py` file contains values that I would like the opportunity to change in the future
- I have them centralized here because it would suck to hunt down every place I used these values if I'd like to change them
- most of these are pretty straight forward:
    - WINDOW_WIDTH/WINDOW_HEIGHT: 768, dims of window
    - VIEW_WIDTH/VIEW_HEIGHT: 64, the dims of  the game grid
    - BORDER: 32, how much padding is on the edges. Ensures symmetry and makes it so that there's a margin
    - FONT: freeserif, the font I use draw text
    - FONT_SIZE: 32, the size I use to draw text
    - FPS_LIMIT: 30, the fps the game runs at. Higher fps makes game too fast look into using ups/delta time
    - LIVES: 3, number of lives you start with
    - SPRITE_WIDTH/SPRITE_HEIGHT: a function of width, and border. the size all sprites other than dirt use

## Helpers
- functions that I think don't need to be methods
- `in_range`: requires 2 actors and optionally a float that's minimum distance. returns true if the euclidian distance between 2 actors is <= the minimum distance
- `gen_coords`: requires a list of actors. returns a valid x and y. Will continually generate x, y in valid area then check if it's within 6 units of another actor. If within 6 units it tries again otherwise that's a valid coordinate and it get's returned. PROBLEMS:
    - not happy with `temp = Actor(None, None, None, None)` but I'm using it because in_range requires an actor. To fix i could change in_range to take an 2 x,y pairs but that feels shit
    - no happy with naive approach to generating valid coords. If I had a DS that contained all valid locs, then I could simply randomly select one instead of generated x,y and checking.

# Game Objects
## Actor
## Earth
## TunnelMan
## Consumables
## Oil

# Game Controller