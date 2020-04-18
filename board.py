# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:56:28 2020

@author: lokopobit
"""

# Load internal libreries
import auxFuns 

class Board(object):
    """
    This class implements the characteristics of a board.
    """
    
    def __init__(self, board):
        """
        This class has only one attribute.
        
        Parameter:
            board : a board (list of lists)
            
        Example: 
            >>> board = Board([[2, 0], [0, 2]])
        """
        
        self.board = board
    