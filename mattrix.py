# You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the 
# bottom right corner?

# You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.

# For example, given the following matrix:

# [[0, 0, 1],
#  [0, 0, 1],
#  [1, 0, 0]]

#  Return two, as there are only two ways to get to the bottom right:

# Right, down, down, right
# Down, right, down, right
# The top left corner and bottom right corner will always be 0.

def count_steps(m, n):
    arr = [[0 for r in range(n)] for c in range(m)]
    for i in range(m):
        arr[i][0] = 1
    for j in range(n):
        arr[0][j] = 1

    # calculate number of steps for other sells
    for r in range(1, m):
        for c in range(1, n):
            arr[r][c] = arr[r-1][c] + arr[r][c-1]
    return arr[m-1][n-1]

print(count_steps(3,4))