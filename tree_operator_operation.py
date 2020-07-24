# This problem was asked by Microsoft.

# Suppose an arithmetic expression is given as a binary tree. Each leaf is 
# an integer and each internal node is one of '+', '−', '∗', or '/'.

# Given the root to such a tree, write a function to evaluate it.

# For example, given the following tree:
# You should return 45, as it is (3 + 2) * (4 + 5).
# using in_order DFS
class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
def return_expression_result(tree_):
    result = 0
    def help(node):
        if node.value.isnumeric():
            return node.value
        left_result = help(node.left)
        right_result = help(node.right)
        res_str = str(left_result) + node.value + str(right_result)
        res_int = eval(res_str)
        return res_int
    res_ = help(tree_)
    return res_
         
tree = Node('*', left = Node('+', Node('3'), Node('2')), right = Node('+', Node('4'), Node('5')))
rre = return_expression_result(tree)
print(rre)
