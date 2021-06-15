# To run this game follow this url : https://py2.codeskulptor.org/#user48_XR46J1Q0vr_9.py

"""
Clone of 2048 game.
Created by GE
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # create a list with 4 zeros
    line_update = [0 for dummy_n in range(len(line))]
    # go through the list 'line' and slide all the not zero numbers 
    # to the left, save the result in the created list 'line_update'
    for posi in range(len(line)):
        if line[posi] != 0:
            for posj in range(len(line)):
                if line_update[posj] == 0:
                    line_update[posj] = line[posi]
                    break
    # merge same number tiles starting from the left and slide everything to 
    # the left after merging, a tile can be merged only once per turn                
    for posi in range(len(line)):
        if posi <= len(line) - 2:
            if line_update[posi] == line_update[posi + 1]:
                line_update[posi] = line_update[posi] + line_update[posi+1]
                line_update.pop(posi + 1)
                line_update.append(0)
    return line_update


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height = 4, grid_width = 4):
        self._grid_h = grid_height
        self._grid_w = grid_width
        self._initial_tiles = {UP: [(0, col) for col in range(self._grid_w)],
                            DOWN: [(self._grid_h - 1, col) for col in range(self._grid_w)],
                            LEFT: [(row, 0) for row in range(self._grid_h)],
                            RIGHT: [(row, self._grid_w - 1) for row in range(self._grid_h)]
                            }
        self.reset()
        
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_w)]for dummy_row in range(self._grid_h)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return str(self._grid)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_h

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_w

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == UP or direction == DOWN:
            for tuple_pair in self._initial_tiles[direction]:
                temp_list = []
                for dummy_i in range(self._grid_h):
                    row = tuple_pair[0] + OFFSETS[direction][0]*dummy_i
                    col = tuple_pair[1] + OFFSETS[direction][1]*dummy_i
                    temp_list.append(self.get_tile(row, col))
               
                merged_list = merge(temp_list)
                for dummy_i in range(self._grid_h):
                    row = tuple_pair[0] + OFFSETS[direction][0]*dummy_i
                    col = tuple_pair[1] + OFFSETS[direction][1]*dummy_i
                    self.set_tile(row, col, merged_list[dummy_i])
        else:
            for tuple_pair in self._initial_tiles[direction]:
                temp_list = []
                for dummy_i in range(0, self._grid_w):
                    row = tuple_pair[0] + OFFSETS[direction][0]*dummy_i
                    col = tuple_pair[1] + OFFSETS[direction][1]*dummy_i
                    temp_list.append(self.get_tile(row, col))
               
                merged_list = merge(temp_list)
                for dummy_i in range(0, self._grid_w):
                    row = tuple_pair[0] + OFFSETS[direction][0]*dummy_i
                    col = tuple_pair[1] + OFFSETS[direction][1]*dummy_i
                    self.set_tile(row, col, merged_list[dummy_i])            
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        rand_coef = random.randrange(0,10)
        temp_iter = 0
        rand_col = 0
        rand_row = 0
        for dummy_i in range(self._grid_h):    
            if 0 in self._grid[dummy_i]:
                while temp_iter < 1:
                    rand_col = random.randrange(0, self._grid_w)
                    rand_row = random.randrange(0, self._grid_h)
                    if self._grid[rand_row][rand_col] == 0:
                        if rand_coef < 9:
                            self._grid[rand_row][rand_col] = 2
                            temp_iter += 1
                        else:
                            self._grid[rand_row][rand_col] = 4
                            temp_iter += 1
                        


    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._row = row
        self._col = col
        self._grid[self._row][self._col] = value
        
    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        self._row = row
        self._col = col
        return self._grid[row][col]
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
