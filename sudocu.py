# Sudoku is a puzzle where 
# you're given a partially-filled 9 by 9 grid with digits. T
# he objective is to fill the grid with the constraint that every row, column, and box 
# (3 by 3 subgrid) must contain all of the digits from 1 to 9.
import numpy as np

grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0], [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3], [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6], [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5], [0, 0, 0, 0, 8, 0, 0, 7, 9]]
np_grid = np.matrix(grid)

def is_possible(y, x, n):
    global grid
    for i in range(0, 9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == n:
                return False
    return True 
print(is_possible(4, 4, 3))

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for i in range(1, 10):
                    if is_possible(y, x, i):
                        grid[y][x] = i
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))

solve()
