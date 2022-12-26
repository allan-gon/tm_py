# Non-Game Objects
## Enums
- generally, I'm using enums as a more expressive way to represent certain values
- strings could suffice but I think having all the values centralized in a class is cleaner
- there's a single file `src/game_enums.py` that contains all of them
- I import Sound, init, and Enum because:
    - `pygame.mixer.Sound`: to load the sound assets and play them later
    - `pygame.init`: because Sound doesn't work if pygame is not initialized
    - `enum.Enum`: to use as the parent class
    - `enum.auto`: to use as the type since I dont care about the type for some enums

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
    - TICK_RATE: 30, the amount of times the game will update per second
    - messages: there isn't a constant called messages but there are several messages grouped together. Used in draw_menu from the view
    - LIVES: 3, number of lives you start with
    - SPRITE_WIDTH/SPRITE_HEIGHT: a function of width, and border. the size all sprites other than dirt use

## Helpers
- functions that I think don't need to be methods
- `in_range`: requires 2 actors and optionally a float that's minimum distance. returns true if the euclidian distance between 2 actors is <= the minimum distance
- `gen_coords`: requires a list of actors. returns a valid x and y. Will continually generate x, y in valid area then check if it's within 6 units of another actor. If within 6 units it tries again otherwise that's a valid coordinate and it get's returned. PROBLEMS:
    - not happy with `temp = Earth(None, None)` but I'm using it because in_range requires an actor. To fix i could change in_range to take an 2 x,y pairs but that feels shit
    - not happy with naive approach to generating valid coords. If I had a DS that contained all valid locs, then I could simply randomly select one instead of generated x,y and checking.

# Game Objects
## Actor
- abstract base class that all game object inherit from
- constructor requires `x: int, y: int, visible: bool, direction: Direction`
- has the following attributes:
    - `is_visible`: used to tell whether or not to draw an object on this tick
    - `is_alive` = True: used to properly clean up actors on a given tick
    - `x`: position
    - `y`: position
    - `direction`: used to properly rotate or flip an asset
    - `img_num` = 0: used if an actor has multiple assets to animate the movement
    - `ticks_elapsed` = 0: used for certain actors that need to behave differently depending on how many ticks have passed by. There's coupling happening here. Not all actors care about ticks but making a class that only differs in that it has a ticks atribute feels wasteful.
- has an abstract method `do_something` where all children will specify what a given actor should do on a tick
- has a method `move_to`. Takes an x and y and set's the actors x,y to that. There is coupling happening here I'm not happy about since not all actors can move. Only tunnelman, regular protester, hardcore protester, boulder, and squirt move. Solution would be create another class that these inherit from but inheritance for a single class or method feels wasteful. There is SOME overlap between tickful and moving actors but not 1:1 so no worth to make a class that's both.
- the assets for a given child are class variables because that's more efficient than loading it every single time it's needed and it just feels more natural that it exists within the class

## Earth
- inherits from actor
- unlike all other children of actor, the image assets get's scaled because earth is 1/4 the size of all other game objects
- the `constructor` only requires an x and y because all earth starts as visible and facing right
- the `do_something` is coulped. Earth doesn't need it but it needs everything else actor needs

## TunnelMan
## Oil
- you'll likely see this in most children of actors. I have forward declerations of the class so that I can use it for type hinting
- another things you'll see a lot is that img or imgs is a class variable. Imgs means that the actor type must be animated so it holds a list of images to switch between. Because all actors except the earth share common dimensions, I defined that in the game constants and use it here.
- `constructor`: only expects and x and y because all oil starts invisible and facing right
- `do_something`: takes a model and view because it's behavior is dependent on tunnelman which resides in the model and also must play a sound for which that functionality exists within the view. All this does is if it's currently invisble check if it's within 4 units of the tunnelman, if it is make it visible. If already visible and within 3 unnits of the tunnel it should die at the end of the tick, play a sound, and increase the score

# GameModel
- this is the container for all the game objects
- `attributes`: state, lives, level, score, earth, boulders, player, sonar, water, squirts, gold, oil
    - `state`: used to figure out what menu to draw or to know to draw the game
    - `lives`: used to chagne state so the game over screen can be drawn
    - `level`: used in a handful of calculations. also used for the HUD
    - `score`: used in the HUD
- `init_earth`: method called when creating a new world (ae. on level start) that correctly makes earth everywhere except shaft and top
- `calc_oil`: method that returns the number of barrels to make on the level according to the formula from the spec
- `create_oil`: method that creates the correct number of oil barrels on level start
<!-- ADD HERE -->
- `create_new_world`: method that calls all of the create methods on level start
- `tick`: method that has each actor do something, cleans up dead actors, adds new actors when relevant, and changes the state if player dies or level ends. Takes two arguments `keys_pressed` and `view`. keys is used to correctly move certain actors and view is needed to play sounds

# GameView
- handles all of the drawing
- has two attributes `window` and `font`. That's a pygame window (ae. the canvas to draw on) and pygame font
- `draw_menu`: method that draws all of the menus. It takes 2 arguments `message_1` and `message_2`. Will draw both strings to screen in two specific spots
- `clear_screen`: method that fills the screen with black
- `draw_actor`: method that given an actor and an image draws ot to screen
- `draw_earth`: method that's a wrapper to draw_actor but since earth is a different shape then eveything else (ae. 2D list) needs to iterate differently
- `draw_actor_container`: method that's a wrapper to draw_actor. Since draw actor expects a single actor (and this is useful for some actors like tunnelman and sonar) I need to loop through a flat list and pass it to draw_actor. It handles both animated actors and non-animated actors because `images` can be a list or a single item and it'll work slightly differently for each
- `draw_world`: method that calls the draw methods on each actor type
- `play_sound`: method that plays the sound passed to it. This is a pygame sound object

# GameController
- the model holds all the data, the view places it on screen, but the controller tells the view what and when the data should be put on screen
- `attributes`: model, view, clock. Clock is just to set the frame rate
- `run`: the only method of the controller class. It's the main game loop