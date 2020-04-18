# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:58:42 2020

@author: lokopobit
"""

# Load external libreries
import random

def random_board(n):
    """
    Returns a board (matrix) of size n with 2 pieces randomly generated.
    
    Parameter:
        n : size of the board (int)
        
    returns:
        randomB : board (list of lists)
        
    Example:
        >>> random_board(2)
        [[0, 0], [4, 2]]
    """
    
    if n > 1:
        randomB = createMatrix(n, n)
        init_values = [2, 2, 2, 4]
        n1 = random.choice(init_values)
        n2 = random.choice(init_values)   
        f1, c1 = random.randint(0, (n-1)), random.randint(0, (n-1))
        f2, c2 = random.randint(0, (n-1)), random.randint(0, (n-1))        
        
        while f1 == f2 and c1 == c2:
            f2, c2 = random.randint(0, (n-1)), random.randint(0, (n-1))           
        
        randomB[f1][c1] = n1
        randomB[f2][c2] = n2
        return randomB    
    
def explicit_board(n, n1, f1, c1, n2, f2, c2):
    """
    Returns a board of size n with value n1 in the cell (f1, c1) and with value
    n2 in the cell (f2, c2).
    
    Parameters:
        n : size of the board (int)
        n1 : value (int)
        f1 : row (int)
        c1 : column (int)
        n2 : value (int)
        f2 : row (int)
        c2 : column (int)
        
    Returns:
        explicitB : board (list of lists)
        
    Example:
        >>> explicit_board(2, 2048, 1, 1, 1024, 0, 0)
        [[1024, 0], [0, 2048]]
    """
    
    explicitB = createMatrix(n, n)
    if 0 <= f1 < n and 0 <= c1 < n and 0 <= f2 < n and 0 <= c2 < n:
        explicitB[f1][c1] = n1
        explicitB[f2][c2] = n2
        return explicitB
    
def bool_matrix(n):
    """
    Returns a matrix of size n with True values.
    
    Parameter:
        n : size of the matrix (int)
    
    Returns:
        boolM : matrix with true values (list of lists)
        
    Example:
        >>> bool_matrix(2)
        [[True, True], [True, True]]         
    """
    
    boolM = createMatrix(n, n)
    for i in range(len(boolM)):
        for j in range(len(boolM)):
            boolM[i][j] = True
    return boolM

def createMatrix(n, m):
    """
    Creates an empty matrix with n rows and m columns.
    
    Parameters:
        n : number of rows (int)
        m : number of columns (int)
        
    Returns:
        matrix : matrix of zeros (list of lists)
        
    Example: 
        >>> createMatrix(2, 2)
        [[0, 0], [0, 0]]
    """
    
    matrix = []
    for i in range(n):
        a = [0]*m
        matrix.append(a)
    return matrix
    
    