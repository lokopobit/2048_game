# 2048_game
OOP implementation of the famous game 2048 in python (GUI is not available)  


## Rules of the game

At the beginning there is a 4x4 board with 2 pieces randomly located. The pieces can be the number 2 or the number 4 (initially). When pressing left, rigth, up or down keys  the pieces move in that direction. If in one of these movements two pieces clash then the become one piece but of double value. After avery movement a new piece appears (with value 2 or 4; value 2 is more probable). The score is updated after each move with the value of the resulting fusion.  

If we try to move in an impossible direction then no new piece is generated.

Next a link to the game: [https://gabrielecirulli.github.io/2048/](https://gabrielecirulli.github.io/2048/)  


## Implementation details  
The game is implemented in pure python so that it is playable with the keyboard  although no GUI is provided.  

The class Game2048 contains the next attributes:  
> A board, that is, a aquared matrix of size n that contains the value of the pieces (0 if they are empty).
> The score of the game
> The maximum value, that is, the maximum value reached by one of the pieces.

The constructor has one single input parameter, the board. The initial value of the score is 0. The next methods are implemented:
> - up(), down(), left(), right() that can do the correspondent movement. Also, these methods must return a boolean if the movement was possible. The score and the maximum value mus be updated.  
> - add_new_cell() generates a new piece randomly. The new value can be 2 with 0.75 probability or 4 with 0.25 probability.  
> - get_value(row, col) return the value of the piece in the cell(row, col), or 0 if it doesn't exist.  
> - put_value(row, col, value) inserts value in the cell(row, col). The cell must be empty for this method to take effect.  
> - get_size() returns the size of the board.  
> - is_blocked() returns true if the board is blocked, that is, no more movements can be done.  
> - max_cell() returns the maximum value of one cell of the board.
> - score() returns the actual score of the game.