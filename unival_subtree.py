# This problem was asked by Google.

# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

# Given the root to a binary tree, count the number of unival subtrees.

# For example, the following tree has 5 unival subtrees:                     
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
def is_unival(root):
    if root is None:
        return True
    if root.left is not None and root.left != root:
        return False
    if root.right is not None and root.right != root:
        return False
    if is_unival(root.left) and is_unival(root.right):
        return True
    return False 
# This is not efficient O(n^2)
def count_univals(root):
    if root is None:
        return 0
    count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        count += 1
    return count
# Efficien solution will be tto unite those two functions for O(n)
def helper(root):
    if root is None:
        return (0, True)
    unival_count_left, is_unival_left = helper(root.left)
    unival_count_right, is_unival_right = helper(root.right)
    is_unival = False
    if not is_unival_left or not is_unival_right:
        is_unival = False
    if root.left is not None and root.left.value != root.value:
        is_unival = False
    if root.right is not None and root.right.value != root.value:
        is_unival = False
    if is_unival:
        return (unival_count_left + unival_count_right + 1, True)
    else:
        return (unival_count_left + unival_count_right, False)


root = Node(3, Node(3), Node(2, Node(2), Node(2)))
print(root)
print(is_unival(root))