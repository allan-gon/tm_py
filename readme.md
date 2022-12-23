# Game Enums
- a more readable way of defining certain values
- `GameState`: if on menu, playing, etc
- `Direction`: the direction a given actor is facing
- `Images`: could have defined constants for images but it feels better to group them all in an enum

# GameController
- runs everything. the main game loop is part of this class and it holds all actors

## Draw
- why so many?
    - each actor class is drawn slightly differently or the number of times an actor class is drawn is diffferent so an interface that calls the actual drawer is useful
- aren't they redundant since you have a draw actor method?
    - as stated above, the drawing is only slightly different in that different assets are used and sizes differ so if I didn't have a single method that can draw everything I'd need one method for each class that look 99% the same
- why not have these methods within each actor?
    - ...
- why does draw always use earth size
    - 64 x 64