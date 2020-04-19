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
        
    def transpose(self):
        """
        Returns the transposed board.
        
        Example:
            >>> board.transpose()
            [[2, 0], [0, 2]]
        """
        
        m = len(self.board)
        n = len(self.board[0])
        transposed = auxFuns.createMatrix(n, m)
        for i in range(n):
            for j in range(m):
                transposed[i][j] = self.board[j][i]

        self.board = transposed
        
    def symmetric(self):
        """
        Returns the symmetric board along the vertical axis.
        
        Example:
            >>> board.symmetric()
            [[0, 2], [2, 0]]
        """
        
        n = len(self.board)
        sym = auxFuns.createMatrix(n, n)
        i = 0
        while i < n:
            j = n - 1
            while j >= 0:
                sym[i][j] = self.board[i][n-j-1]
                j -= 1
            i += 1

        self.board = sym
        
    def blank_squares(self):
        """
        Returns the empty cells of a board.
        
        Example:
            >>> board.blank_squares()
            [(0, 1), (1, 0)]
        """
        
        l = []
        i = 0
        while i < len(self.board):
            j = 0
            while j < len(self.board):
                if self.board[i][j] == 0:
                    l.append((i, j))
                j += 1
            i += 1
        return l
        
        