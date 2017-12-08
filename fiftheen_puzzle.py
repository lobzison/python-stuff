"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

#import poc_fifteen_gui


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

        self._moves = {"down": "lddru",
                       "right": "urrdl",
                       "left": "ulldr",
                       "u_to_l": "ld",
                       "u_to_r": "rd",
                       "r_to_u": "ul",
                       "l_to_u": "ur"}

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        zero_in_pos = self.get_number(target_row, target_col) == 0
        lower_rows = True
        righter_cells = True
        if target_row != self.get_height() - 1:
            for rows in range(target_row + 1, self.get_height()):
                for cols in range(self.get_width()):
                    check = self.current_position(rows, cols) == (rows, cols)
                    lower_rows = lower_rows and check
        if target_col != self.get_width() - 1:
            for cols in range(target_col, self.get_width()):
                check = self.current_position(target_row, cols) == (target_row,
                                                                    cols)
                righter_cells = righter_cells and check
        return zero_in_pos and lower_rows

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # replace with your code
        assert self.lower_row_invariant(target_row, target_col), (
            "lower_row_invariant failed at %d %d" % (target_row, target_col))
        # find where the target tail is, move zero to that position
        target_pos = self.current_position(target_row, target_col)
        res = self.move_to_target_out((target_row, target_col), target_pos)

        # check where there target cell is now, get all distances
        current_pos = self.current_position(target_row, target_col)
        zero_pos = self.current_position(0, 0)
        z_row_diff = zero_pos[0] - current_pos[0]
        z_col_diff = zero_pos[1] - current_pos[1]
        t_row_diff = target_row - current_pos[0]
        t_col_diff = target_col - current_pos[1]
        t_diff = [t_row_diff, t_col_diff]
        z_diff = [z_row_diff, z_col_diff]
        print self.zero_to_target(z_diff)

        # replace with proper while
        # for i in range(2):
        if current_pos[1] > target_col:
            pass    # implement later
        # else:
        #     while not (current_pos[0] == target_row and
        #                current_pos[1] == target_col):
        #     if

        # self.update_puzzle(move)
        # i = 0
        # print self
        # while not (current_pos[0] == target_row and
        #            current_pos[1] == target_col):

        #     if (z_col_diff == 0 and target_row > current_pos[0] and
        #             target_col <= current_pos[1]):
        #         print "target is uder 0, implement move down"
        #         move = self._moves["down"]
        #     elif z_col_diff < 0 and target_col < current_pos[1]:
        #         print "target is to the right 0, implement move right"
        #         move = self._moves["right"]
        #     else:
        #         print "target is to the left 0, implement move left"
        #         move = self._moves["left"]
        #     self.update_puzzle(move)
        #     print self, move
        #     res += move
        #     current_pos = self.current_position(target_row, target_col)
        #     zero_pos = self.current_position(0, 0)
        #     z_col_diff = zero_pos[1] - current_pos[1]
        #     # z_row_diff = zero_pos[0] - current_pos[0]

        #     i += 1
        #     if i > 100:
        #         break
        return res

    def move_to_dir(self, direction, position):
        res = ""
        if direction == position:
            res += position[0]
        if direction == "down":
            if position == 
        return res

    def move_to_target_out(self, zero_coord, target_coord):
        """
        Moves zero tile to target tile.
        Returns stirng with moves
        """
        res = ""
        ups = zero_coord[0] - target_coord[0]
        lefts = zero_coord[1] - target_coord[1]
        if target_coord[1] > zero_coord[1] and ups > 0:
            res += "u"
            ups -= 1
        if lefts > 0:
            res += "l" * lefts
        else:
            res += "r" * -lefts
        res += "u" * ups
        self.update_puzzle(res)
        return res

    def zero_to_target(self, z_diff):
        """
        Returns where zero tile is
        with respect to target tile
        """
        res = None
        if z_diff[0] == 0:
            if z_diff[1] == 1:
                res = "right"
            if z_diff[1] == -1:
                res == "left"
        elif z_diff[1] == 0:
            if z_diff[0] == -1:
                res = "up"
            if z_diff[0] == 1:
                res = "down"
        return res

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        # replace with your code
        return False

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""


# Start interactive simulation
#poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
