# There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner 
# and getting to the bottom-right corner. You can only move right or down.

# For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

# Right, then down
# Down, then right
# Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
# dynamic aproach with memoisation
def find_ways_from_left_to_right(matrix):
    rows_count = len(matrix)
    column_count = len(matrix[0])
    result_matrix = [[0 for j in range(column_count)] for i in range(rows_count)]
    r_i, c_i = 0, 0
    for i in range(rows_count):
        for j in range(column_count):
            if i == 0 or j == 0:
                result_matrix[i][j] = 1
            else:
                result_matrix[i][j] = result_matrix[i - 1][j] + result_matrix[i][j - 1]

    return result_matrix[rows_count - 1][column_count - 1]

sol = find_ways_from_left_to_right([[1, 2], [3, 4], [3, 4]])
print(sol)
