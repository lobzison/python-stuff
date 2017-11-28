"""
Clone of 2048 game.
"""

import random
#import poc_2048_gui

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
    Function that merges a single row or column in 2048.
    """
    # replace with your code
    res = move(list(line))
    for idx in range(len(line) - 1):
        if res[idx] != 0 and res[idx] == res[idx + 1]:
            res[idx], res[idx + 1] = res[idx] + res[idx + 1], 0

    res = move(res)
    return res


def move(line):
    """
    Function that moves numbers in list to the left
    :type line: list
    """
    if 0 in line:
        res = [0 for _ in line]
        index = 0
        for num in line:
            if num != 0:
                res[index] = num
                index += 1
        return res
    else:
        return line


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()
        up_ = [(0, num) for num in range(self._grid_width)]
        down = [(self._grid_height - 1, num) for num in range(self._grid_width)]
        left = [(num, 0) for num in range(self._grid_height)]
        right = [(num, self._grid_width - 1) for num in range(self._grid_height)]
        self._starting_tiles = {UP: up_,
                               DOWN: down,
                               LEFT: left,
                               RIGHT: right}

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for _ in range(self._grid_width)] for _ in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        res = ""
        for row in self._grid:
            res += str(row) + '\n'
        return str(res)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        is_moved = False
        starting_line = self._starting_tiles[direction]
        offset = OFFSETS[direction]

        for tile in starting_line:
            tile_init = list(tile)
            line_to_merge = []
            if direction in (UP, DOWN):
                num_steps = self.get_grid_height()
            else:
                num_steps = self.get_grid_width()
            for _ in range(num_steps):
                line_to_merge.append(self.get_tile(tile_init[0], tile_init[1]))
                tile_init[0] += offset[0]
                tile_init[1] += offset[1]

            merged_line = merge(line_to_merge)
            if merged_line != line_to_merge:
                is_moved = True

            tile_init = list(tile)
            for num in merged_line:
                self.set_tile(tile_init[0], tile_init[1], num)
                tile_init[0] += offset[0]
                tile_init[1] += offset[1]

        if is_moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        tile_value = random.randrange(11)
        if tile_value == 10:
            tile_value = 4
        else:
            tile_value = 2
        empty_tiles = []
        for r_index, row in enumerate(self._grid):
            for c_index, col in enumerate(row):
                if col == 0:
                    empty_tiles.append((r_index, c_index))
        empty_tile = random.choice(empty_tiles)
        self.set_tile(empty_tile[0], empty_tile[1], tile_value)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]

#poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

