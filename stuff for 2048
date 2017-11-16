import random
HEIGHT  = 5

WIDTH = 6

grid = [[0 for i in range(WIDTH)] for j in range(HEIGHT)]

print grid

empty_cells = set([])

print [grid.index(row) for row in grid]

print [i for i, x in enumerate(grid)]

for r_index, row in enumerate(grid):
    for c_index, col in enumerate(row):
        empty_cells.add((r_index, c_index))

print(empty_cells)


b = [(r_index, c_index) for c_index, col in enumerate(row)
                        if col == 0
                        for r_index, row in enumerate(grid)]

c = random.choice(b)

print(c)
