## minesweeper

### think of an idea

I like the idea of minesweeper. It'll be available to anyone downloading the source code. The program will have a graphical interface with buttons to press with either left of right clicks. You can win the game with an acknowledgement or loose when you click a bomb. I will not include a counter for how many bombs are left, not the smiley face atop an old-style Windows minesweeper game. The game will just have the provided amount of tiles and an amount of bombs relative to a difficulty parameter.

Input values: size (rows, columns), difficulty (easy, medium, hard).

### project brainstorming

The game is a one-player game with .py files for main, board, game and tile. It relies on user input for the board size and the difficulty rating.

Key functionality:
- draw board
- include random bombs on board
- include number identifiers for number of surrounding bombs
- hide bombs and numbers
- allow flagging toggle, unable to click when flagged
- allow clicking to reveal tile
- clear up fields not adjacent to bombs when clicked
- stop game once bomb is clicked
- win game once all bombs are identified

Functions to include in 

#### board:
- initialize
- load pictures
- draw board (open/hidden)
- update board (adjacent clear tiles clear up as well)

#### game:
- initialize
- left click event
- right click event
- lost event
- win event

#### tile:
- initialize
- clicked or not clicked
- flagged or not flagged
- 

### refactoring

### blog post

To be able to run the software you need to install Python and pygame and Pillow