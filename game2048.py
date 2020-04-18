# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:03:23 2020

@author: lokopobit
"""

# Load internal libreries
import random
from board import Board

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
        self.socre = score
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


#class board        
        