import fiftheen_puzzle
import poc_simpletest


my_suite = poc_simpletest.TestSuite()


grid = [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]
my_puzzle = fiftheen_puzzle.Puzzle(3, 3, grid)

my_suite.run_test(my_puzzle.lower_row_invariant(0, 0), True)


#grid2 = [[3, 8, 1, 5, 0],
         # [4, 2, 6, 7, 9],
         # [10, 11, 12, 13, 14],
         # [15, 16, 17, 18, 19],
         # [20, 21, 22, 23, 24]]

#my_puzzle2 = fiftheen_puzzle.Puzzle(5, 5, grid2)
#print my_puzzle2.solve_row0_tile(4)
#print my_puzzle2
# print my_puzzle2
# print my_puzzle2.solve_col0_tile(2)
# print my_puzzle2

# gird3 = [[0, 6, 2, 3, 4],
#          [1, 5, 7, 8, 9],
#          [10, 11, 12, 13, 14],
#          [15, 16, 17, 18, 19]]

# my_puzzle3 = fiftheen_puzzle.Puzzle(4, 5, gird3)
# print my_puzzle3
# print my_puzzle3.solve_2x2()
# print my_puzzle3
grid3 = [[4, 3, 2],
         [1, 0, 5],
         [6, 7, 8]]


my_puzzle3 = fiftheen_puzzle.Puzzle(3, 3, grid3)
my_puzzle3.solve_puzzle()
print my_puzzle3


#my_puzzle2 = fiftheen_puzzle.Puzzle(3, 3, gird3)
# print my_puzzle2.solve_col0_tile(2)
#Puzzle(4, 5, [[1, 2, 0, 3, 4], [6, 5, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19]]), obj.solve_row0_tile(2)
#my_suite.run_test(my_puzzle2.solve_interior_tile(2, 2), True)

my_suite.report_results()
