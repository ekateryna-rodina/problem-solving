# This problem was asked by Google.

# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, 
# and deserialize(s), which deserializes the string back into the tree.

# For example, given the following Node class

# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:

# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'
from collections import deque
class Node:
    def __init__(self, val, left_ = None, right_ = None):
        self.val = val
        self.left = left_
        self.right = right_ 
    def set_value(self, value):
        self.val = value
    def get_value(self):
        return self.val
    def set_left(self, val):
        self.left = Node(val)
    def set_right(self, val):
        self.right = Node(val)
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def has_left(self):
        return self.left is not None
    def has_right(self):
        return self.right is not None
    
    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"
    

class Tree:
    def __init__(self, value):
        self.root = Node(val=value)
        self.stack = list()
    def get_root(self):
        return self.root
    def traverse(self, node: Node, result: str):
        self.stack.append(node)
        while len(self.stack) > 0:
            last = self.stack.pop()
            if last == None:
                result += "# "
                continue
            self.stack.append(last.get_right())
            self.stack.append(last.get_left())
            result += "{} ".format(last.get_value())
        return result

    def serialize(self):
        '''
        Serializes a tree to a string
        '''
        result = ""
        result += self.traverse(self.get_root(), result)
        return result
               
    def deserialize(self, str_to_deserialize):
        '''
        Derializes a string to a tree
        '''
        def traverse():
            val = next(vals)
            if val == '#':
                return
            new_node = Node(val)
            new_node.left = traverse()
            new_node.right = traverse()
            return new_node

        vals = iter(str_to_deserialize.split(" "))
        return traverse()
            
# tree = Tree('apple')
# tree.get_root().set_left('banana')
# tree.get_root().set_right('cherry')
# (tree.get_root().get_left()).set_left('dates')
# (tree.get_root().get_right()).set_left('straberry')
# (tree.get_root().get_right()).set_right('blueberry')

# print(tree)
# bb = tree.serialize()
# new_t = tree.deserialize(bb)
# print(new_t)
