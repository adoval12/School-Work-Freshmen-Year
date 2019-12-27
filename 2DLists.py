#
# ps7pr2.py (Problem Set 7, Problem 2)
#
# 2-D Lists
#
#

import random

def create_grid(height, width):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: height and width are non-negative integers
    """
    grid = []
    
    for r in range(height):
        row = [0] * width     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line, and nothing between values.
        input: grid is a 2-D list. We assume that all of the cell
               values are integers between 0 and 9.
    """
    height = len(grid)
    width = len(grid[0])
    
    for r in range(height):
        for c in range(width):
            print(grid[r][c], end='')   # print nothing between values
        print()                         # at end of row, go to next line

#
# Function 0:diagonal_grid(height, width)
#

def diagonal_grid(height, width):
    """ creates and returns a height x width grid in which the cells
        on the diagonal are set to 1, and all other cells are 0.
        inputs: height and width are non-negative integers
    """
    grid = create_grid(height, width)   # initially all 0s

    for r in range(height):
        for c in range(width):
            if r == c:
                grid[r][c] = 1
    return grid


#
# Function 1: inner_grid(height, width)
#

def inner_grid(height, width):
    """Input a height and a width and the function will return a 2-D list of
       height rows and width columns in which the “inner” cells are all 1 and the
       cells on the outer border are all 0."""
    grid = create_grid(height, width)
    for r in range(1, (height - 1)):
        for c in range(1, (width - 1)):
            grid[r][c] = 1
    return grid

#
# Function 2: random_grid(height, width)
#

def random_grid(height, width):
    """Input a height and a width and the function will return a returns a
       2-D list of height rows and width columns in which the inner cells are
       randomly assigned either 0 or 1, but the cells on the outer border are
       all 0."""
    grid = create_grid(height, width)
    for r in range(1, (height - 1)):
        for c in range(width):
            grid[r][c] = random.choice([0, 1])
    return grid

#
# Function 3: copy(grid)
#

def copy(grid):
    """ Input a grid and the function will return a new, separate 2-D list
        that has the same dimensions and cell values as grid"""
    new_grid = create_grid(len(grid), len(grid[0]))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if new_grid[r][c] != grid[r][c]:
                new_grid[r][c] = grid[r][c]
    return new_grid

#
# Function 4: invert(grid)
#

def invert(grid):
    """Input a grid and the function will change all its one to zeroes and
       all its zeroes to ones"""
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                grid[r][c] = 1
            else:
                grid[r][c] = 0
                
    
            
        
    
    
    
    


            
                
                
            
        
    

