# recursional approach
def count_islands_rec(matrix = []):
    row_pointer = 0
    column_pointer = 0
    islands_count = 0
    # base case
    if len(matrix) == 0:
        return
    # iterating through matrix
    for r in range(0, len(matrix)):
        for j in range(0, len(matrix[r])):
            if matrix[r][j] == 1:
                # increase count of islands
                islands_count += 1
                # update 1 to 0
                update_island_to_water(matrix, r, j)
    return islands_count

def update_island_to_water(matrix, row, column):
    # base case
    # - if row < 0
    # - if row > len(matrix)
    # - if column < 0
    # - if column > len(matrix.column)
    # - if value == 0
    if row < 0 or column < 0 or row > len(matrix) - 1 or column > len(matrix[row]) - 1:
        return
    if matrix[row][column] == 0:
        return
    # update island to water
    matrix[row][column] = 0
    # update island horizontally and vertically
    update_island_to_water(matrix, row, column + 1 )
    update_island_to_water(matrix, row, column - 1)
    update_island_to_water(matrix, row + 1, column)
    update_island_to_water(matrix, row - 1, column)


def count_islands_dfs(matrix):
    if len(matrix) == 0:
        return
    max_region = 0
    for row in range(0, len(matrix)):
        for column in range(0, len(matrix[row])):
            if matrix[row][column] == 1:
                size = get_region_size(matrix, row, column)
                max_region = max(size, max_region)
    return max_region

def get_region_size(matrix, row, column):
    if row < 0 or column < 0 or row > len(matrix) - 1 or column > len(matrix[row]) - 1:
        return
    if matrix[row][column] == 0:
        return
    matrix[row][column] = 0
    total_size = 1
    for r in list(range(row - 1, row + 2)):
        for c in list(range(column - 1, column + 2)):
            if r == row and c == column:
                continue
            size = get_region_size(matrix, r, c)
            if size is not None:
                total_size = total_size + size
    return total_size
    

matrix=[[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1]]
count_islands_dfs(matrix)



