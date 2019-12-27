#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Conway's Game of Life
#
#

from 2Dlists import *
from gol_graphics import *
import random

#
# function 1:count_neighbors(cellr, cellc, grid)
#

def count_neighbors(cellr, cellc, grid):
    """ Input the loaction of the cell and the grid it is in and the function will
        return the amount of numbers that are alibe by the cell"""
    count = 0
    if grid[(cellr - 1)][(cellc - 1)] == 1:
        count += 1
    if grid[(cellr - 1)][cellc] == 1:
        count += 1
    if grid[(cellr - 1)][(cellc + 1)] == 1:
        count += 1
    if grid[cellr][(cellc - 1)] == 1:
        count += 1
    if grid[cellr][(cellc + 1)] == 1:
        count += 1
    if grid[(cellr + 1)][(cellc - 1)] == 1:
        count += 1
    if grid[(cellr + 1)][cellc] == 1:
        count += 1
    if grid[(cellr + 1)][(cellc + 1)] == 1:
        count += 1
    return count

def next_gen(grid):
    """This function takes a 2-D list called grid that represents the current generation of
       cells, and that uses the rules of the Game of Life (see above) to create and return a
       new 2-D list representing the next generation of cells."""
    new_grid = copy(grid)
    for r in range(1, (len(new_grid) - 1)):
        for c in range(1, (len(new_grid[0]) - 1)):
            if count_neighbors(r, c, grid) > 3:
                new_grid[r][c] = 0
            if count_neighbors(r, c, grid) < 2:
                new_grid[r][c] = 0
            if count_neighbors(r, c, grid) == 3:
                new_grid[r][c] = 1
    return new_grid 
            
            
            
