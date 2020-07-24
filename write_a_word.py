# This problem was asked by Microsoft.

# Given a 2D matrix of characters and a target word, write a function that returns whether the 
# word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:
# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]
# and the target word 'FOAM', you should return true, since it's the leftmost column. 
# Similarly, given the target word 'MASS', you should return true, since it's the last row.

def find_word(matrix, target):
    if len(target) == 0:
        return False
    row_c = len(matrix)
    col_c = len(matrix[0])
    def helper(row_i, col_i, ind):
        # base case
        if matrix[row_i][col_i] == target[ind]:
            ind = ind + 1
        if row_i == row_c - 1 and col_i == col_c - 1:
            return ind == len(target) - 1
        if col_i == col_c - 1:
            return False
        if row_i == row_c - 1:
            return False

        
        to_r = helper(row_i, col_i + 1, ind)
        if to_r == False:
            col_i = 0
        to_down = helper(row_i + 1, col_i, ind)
        return to_down

    return helper(0, 0, 0)
mart = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
find_word(mart, 'MASS')
        



        

