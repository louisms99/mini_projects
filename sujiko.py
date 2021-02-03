# -*- coding: utf-8 -*-
"""
@author: louismiranda-smedley
"""


import numpy as np

class Sujiko():
    ''' Class for Sujiko solver '''
    
    def __init__(self,grid,sums):
        ''' grid is 2d array '''
        self.grid = grid
        self.sums = sums
        
    def __repr__(self):
        ''' represents grid in puzzle form '''
        print(np.matrix(self.grid)) #represents in nice format
        
    def check(self,y,x,n):
        
        
        for i in range(3):
            for j in range(3):
                if self.grid[i][j] == n:
                    return False
        
        return True
    
    def zones(self,sums):
        ''' sum check '''
        
        zone1 = grid[0][0] + grid[0][1] + grid[1][0] + grid[1][1]
        zone2 = grid[0][1] + grid[0][2] + grid[1][1] + grid[1][2]
        zone3 = grid[1][0] + grid[1][1] + grid[2][0] + grid[2][1]
        zone4 = grid[1][1] + grid[1][2] + grid[2][1] + grid[2][2]
        
        if [zone1,zone2,zone3,zone4] == sums:
            return True
        
        return False
                                                             
        
    def solve(self):
        ''' solves puzzle '''        
        
        for y in range(3):
            for x in range(3):
                if grid[y][x]==0:
                    for n in range(1,10):
                        if self.check(y,x,n):
                            self.grid[y][x] = n
                            self.solve()
                            self.grid[y][x] = 0
                    return
        
        if self.zones(sums):
            print(np.matrix(self.grid))
            
        else:
            return
        
if __name__ == '__main__':
    
    grid = [[0,0,0],
            [0,0,0],
            [6,5,0]]
    
    sums = [10,22,15,21]
    
    Sujiko(grid,sums).solve()


        
    
        

            
            
            
        
                    
        
        
    
        

        
        
        

