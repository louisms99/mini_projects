# -*- coding: utf-8 -*-
"""
@author: louismiranda-smedley
"""


import numpy as np

class Sudoku():
    ''' Class for Sudoku solver'''
    
    def __init__(self, puzzle):
        ''' puzzle : 2D array '''
        self.puzzle = puzzle
    
    
    def __repr__(self):
        ''' represents puzzle '''
        print(np.matrix(self.puzzle))


    def check(self,x,y,n):
        ''' check if number is possible'''
        #check row
        for i in range(9):
            if self.puzzle[y][i] == n:
                return False
        
        #check column
        for i in range(9):
            if self.puzzle[i][x] == n:
                return False
            
        #check zone
        if y <= 2:
            if x <= 2:
                zone = [2,2]
            elif x <= 5:
                zone = [5,2]
            else: zone = [8,2]
        elif y <= 5:
            if x <= 2:
                zone = [2,5]
            elif x <= 5:
                zone = [5,5]
            else: zone = [8,5]
        else:
            if x <= 2:
                zone = [2,8]
            elif x <= 5:
                zone = [5,8]
            else: zone = [8,8]
            
        [x,y] = zone
        
        for i in range(3):
            if self.puzzle[y][x-i] == n:
                return False
            elif self.puzzle[y-1][x-i] == n:
                return False
            elif self.puzzle[y-2][x-i] == n:
                return False
        return True
    
    
    def solver(self):
        ''' solves puzzle '''

        
        for y in range(9):
            for x in range(9):
                if self.puzzle[y][x] == 0:
                    for n in range(1,10):
                        if self.check(x,y,n):
                            self.puzzle[y][x] = n
                            self.solver()
                            self.puzzle[y][x] = 0
                    return
        print(np.matrix(grid))
        input('More solutions?')
 
    
            
class EasyGrid:
    
    def __init__(self):
        
        self.puzzle = np.zeros((9,9))
    
    def display(self):
        return self.puzzle
    
    def generate(self):
        
        for i in range(9):
            k = np.random.randint(low=1,high=9)
            self.puzzle[i][i] = k
        
        print(self.puzzle)
        return self.puzzle
        
        
    
        
    



if __name__ == '__main__':
    
    grid = [[0, 0, 2, 0, 1, 0, 4, 0, 0],
            [0, 0, 0, 3, 5, 9, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 0, 6],
            [0, 9, 0, 5, 0, 0, 0, 3, 0],
            [8, 6, 0, 0, 0, 0, 0, 5, 2],
            [0, 2, 0, 0, 0, 6, 0, 7, 0],
            [9, 0, 0, 0, 0, 0, 0, 0, 7],
            [0, 0, 0, 7, 2, 1, 0, 0, 0],
            [0, 0, 1, 0, 4, 0, 8, 0, 0]]
    
    
    #Sudoku(grid).__repr__()
    Sudoku(grid).solver()


    



# def make_grid():
#    grid = np.zeros((9,9))
#    print(grid)
#    for y in range(9):
#        for x in range(9):    
#            num = input('enter number \n')
#            grid[y][x] = num
#            print(grid)
#    solver(grid)
    



                    


