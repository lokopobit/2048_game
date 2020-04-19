# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:03:23 2020

@author: lokopobit
"""

# Load external libreries
import random

# Load internal libreries
from board import Board
import auxFuns

class Game2048(object):
    """
    This class implements the 2048 game functionality.
    """
    
    def __init__(self, board, score=0, maxValue=0):
        """
        The class has three atributtes: the board, the score and the maximum 
        value reached by one of the pieces.
        
        Parameters:
            board : a board (list of lists)
            score : score of the game, initially is zero (int)
            maxValue : maximum value reached by one of the pieces, initially 
            is zero (int)
            
        Example:
            >>> game = Game2048([[0, 2], [4, 0]])
        """
        
        self.board = board
        self.score = score
        self.maxValue = maxValue
        
    def get_size(self):
        """
        Returns the size of the board.
        
        Example:
            >>> game.get_size()
            2
        """
        
        return len(self.board)
    
    def max_cell(self):
        """
        Returns the maximun value of the board.
        
        Example:
            >>> game.max_cell()
            4
        """
        
        return self.maxValue
    
    def score(self):
        """
        Returns the score of the game.
        
        Example:
            >>> game.score()
            0
        """
        
        return self.score
    
    def is_blocked(self):
        """
        Returns True if the board is blocked or False in other case.
        
        Example:
            >>> game.is_blocked()
            False        
        """
        
        game = Game2048(self.board, self.score, self.maxValue)
        a, b, c, d = game.right(), game.left(), game.up(), game.down()
        if not a:
            if not b:
                if not c:
                    if not d:
                        return True
        return False       
    
    def add_new_cell(self):
        """
        Generates a new piece randomly.
        
        Example:
            >>> game.add_new_cell()
            [[0, 2], [2, 4]]
        """
        
        board = Board(self.board)
        l = [2, 2, 2, 4]
        lista = board.blank_squares()
        aux0 = random.choice(l)
        aux1 = random.choice(lista)
        self.board[aux1[0]][aux1[1]] = aux0
        
    def get_value(self, row, col):
        """
        Return the value of the piece in the cell (row, col)
        
        Parameters:
            row : row of the matrix (int)
            col : column of the matrix (int)
            
        Returns: the value of that piece            
        
        Example:
            >>> game.get_value(0 ,0)            
            0
        """

        if row >= 0 and col >= 0 and row < len(self.board) and col < len(self.board):
            return self.board[row][col]

    def put_value(self, row, col, value):
        """
        Inserts value in the cell (row, col) only in case this cell is empty.
        
        Parameters:
            value : value of the piece (int)
            row : row of the matrix (int)
            col : column of the matrix (int)
            
        Example:
            >>> game.put_value(0, 0, 2048)
            [[2048, 2], [4, 0]]
        """
        
        if self.board[row][col] == 0:
            self.board[row][col] = value
            if value > self.maxValue:
                self.maxValue = value
                
    def right(self):
        """
        Performs the right movement and return True in case the move was done.
        
        Returns: True or False
        
        Example:
            >>> game.right()
            True
        """
        
        boo = auxFuns.bool_matrix(len(self.board))
        i, boole3 = 0, False
        while i < len(self.board):
            j, boole2 = len(self.board)-2, False
            while j >= 0:
                if self.board[i][j] == 0:
                    j -= 1
                else:
                    z, boole = 0, True
                    while z < len(self.board) and boole:
                        if j < (len(self.board)-1) and self.board[i][j+1] == 0:
                            self.board[i][j+1] = self.board[i][j]
                            self.board[i][j] = 0
                            boole2 = True
                            j += 1
                        elif j < (len(self.board)-1) and boo[i][j+1] and self.board[i][j] == self.board[i][j+1]:
                            boo[i][j+1] = False
                            self.board[i][j+1] = 2*self.board[i][j]
                            self.board[i][j] = 0
                            self.score += self.board[i][j+1]
                            boole2 = True
                        else:
                            boole = False
                        z += 1
                    if boole2:
                        boole3 = True
                    j -= 1
            i += 1

        laux = []
        for row in self.board:
            laux.append(max(row))
        self.maxValue = max(laux)

        return boole3
    
    def down(self):
        """
        Performs the down movement and return True in case the move was done.
        
        Returns: True or False
        
        Example:
            >>> game.down()
            False              
        """

        aux = Board(self.board)
        aux.transpose()
        self.board = aux.board
        boole2 = self.right()
        aux.board = self.board
        aux.transpose()
        self.board = aux.board
        return boole2        
    
    def left(self):
        """
        Performs the left movement and return True in case the move was done.
        
        Returns: True or False
        
        Example:
            >>> game.left()
            True              
        """
        
        aux = Board(self.board)
        aux.symmetric()
        self.board = aux.board
        boole2 = self.right()
        aux.board = self.board
        aux.symmetric()
        self.board = aux.board
        return boole2   

    def up(self):
        """
        Performs the up movement and return True in case the move was done.
        
        Returns: True or False
        
        Example:
            >>> game.up()
            False              
        """
        
        aux = Board(self.board)
        aux.transpose()
        aux.symmetric()
        self.board = aux.board
        boole2 = self.right()
        aux.board = self.board
        aux.symmetric()
        aux.transpose()
        self.board = aux.board
        return boole2
    
    def __str__(self):
        """
        Game display

        Example:
            >>> print game
            2    0
            4    0
        """
        res = ''
        size = self.get_size()
        for row in xrange(size):
            for col in xrange(size):
                res += '{0:5}'.format(self.get_value(row, col))
            res += '\n'
        res += '{0:6}-{1:6}'.format(self.max_cell(), self.score())
        return res