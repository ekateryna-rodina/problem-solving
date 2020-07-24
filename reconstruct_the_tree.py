
# Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

# For example, given the following preorder traversal:

# [a, b, d, e, c, f, g]

# And the following inorder traversal:

# [d, b, e, a, f, c, g]

# You should return the following tree:

# lwft ind = root*2 + 1
# right ind = root*2 + 2         
# agorithm
# 1. add preorder into stack
# 2. add inorder into queue
class Node: 
    def __init__(self,value = None, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

def reconstuct_tree(preorder, in_order):
    preorder_index = 0
    in_order_index = 0
    result = {}
    tree_length = len(preorder)
    def traverse(preorder_index, in_order_array):
        if len(in_order_array) == 1:
            return (in_order_array[0], preorder_index)
        index_root = in_order_array.index(preorder[preorder_index])
        new_node = Node(preorder[preorder_index])
        left_result = in_order_array[:index_root]
        right_result = in_order_array[index_root + 1:]  
        left_node, index = traverse(preorder_index + 1, left_result)
        new_node.left = Node(left_node)
        right_node, ind = traverse(index + 1, right_result)
        new_node.right = Node(right_node)
        return (new_node, ind)
    return traverse(0, in_order)
preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
in_order = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
res = reconstuct_tree(preorder, in_order)
print(res)
                                       