# minesweeper

## think of an idea

I like the idea of minesweeper. It'll be available to anyone downloading the source code. The program will have a graphical interface with buttons to press with either left of right clicks. You can win the game with an acknowledgement or loose when you click a bomb. I will not include a counter for how many bombs are left, not the smiley face atop an old-style Windows minesweeper game. The game will just have the provided amount of tiles and an amount of bombs relative to a difficulty parameter.

Input values: size (rows, columns), difficulty (easy, medium, hard).

## project brainstorming

The game is a one-player game with .py files for the classes main, board, game and tile. It relies on user input for the board size and the difficulty rating.

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

### board:
- initialize
- load pictures
- draw board (open/hidden)
- update board (adjacent clear tiles clear up as well)

### game:
- initialize
- left click event
- right click event
- lost event
- win event

### tile:
- initialize
- clicked or not clicked
- flagged or not flagged

## refactoring
At first iteration of a working game, I still needed to implement a win event showing unclicked bombs and playing the win.wav. I also still need feedback for when a tile was wrongly flagged as a bomb. Lastly, I need to rely on user input for the board dimensions (number of tiles).

## blog post

To be able to run the software you need to install Python, Pillow and tkinter.

I ended up leaving out the tile class. All that was needed was in board and game. I had trouble with tkinter's grid function, as it doesn't work together with pack. I had to work with grid solely. The callback functions for the mouse clicks were also tough. I couldn't get a hold of the events variables and therefore I couldn't properly initialize Game with `__init__` variables. That's because `self` had to always refer to Board. This caused much repeated code in changing the tile's appearance.

The code is not very elegant and somewhat hardcoded. Changes I made to the functions pertaining to each class were:

- update board in game.py instead of board.py
- draw board only hidden in board.py, define the open board values in game.py
- click/not-clicked and flagged/not-flagged in game.py

Additional functions I didn't see ahead of time:

- user input for dimensions
- size of the board in pixels
- resize images depending on size of board
- reveal events vs. neighbor testing vs. automatic reveal events
- an array for bombs and tiles with number that reflect the number of surrounding bombs