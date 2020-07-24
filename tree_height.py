class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.visited_left = False
        self.visited_right = None

    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def get_left_node(self):
        return self.left
    def get_right_node(self):
        return self.right
    def set_left_node(self, value):
        self.left = Node(value)
    def set_right_node(self, value):
        self.right = Node(value)
    def has_left_node(self):
        self.left is not None
    def has_right_node(self):
        self.right is not None
    def get_visited_left(self):
        return self.visited_left
    def get_visited_right(self):
        return self.visited_right
    def set_visited_left(self, is_visited):
        self.visited_left = is_visited
    def set_visited_right(self, is_visited):
        self.visited_right = is_visited
    
    def __repl__(self):
        return f'Node value is {self.get_value()}'
    def __str__(self):
        return f'Node value is {self.get_value()}'

class Tree:
    def __init__(self, value = None):
        self.tree = Node(value)

    def get_root(self):
        return self.tree

    def count_univals(self):
        if self.tree.value is None:
            return 0
        
        count = self.is_subtree_uni(self.tree)[0]
        return count

    def is_subtree_uni(self, node):
        if node is None:
            return (0, False)
        if node.left is None and node.right is None:
            return (1, True)     
        count_left, is_left_uni = self.is_subtree_uni(node.left)
        count_right, is_right_uni = self.is_subtree_uni(node.right)
        total_univals = count_left + count_right
        if not is_left_uni or not is_right_uni:
            return (total_univals, False) 
        if node.value != node.left.value:
            return (total_univals, False)
        if node.value != node.right.value:
            return (total_univals, False)

        return (total_univals + 1, True)

class Stack:
    def __init__(self):
        self.list = list()
    def push(self, value):
        self.list.append(value)
    def pop(self, value):
        return self.list.pop()
    def top(self):
        if not is_empty:
            return self.list[-1]
        else:
            return None
    def is_empty(self):
        return len(self.list) > 0

    def __repl(self):
        if not is_empty():
            s = "top of stack".join([str(item) for item in self.list[::-1]])
            return s


tree = Tree(3)
tree.get_root().set_left_node(2)
tree.get_root().set_right_node(3)
tree.get_root().get_right_node().set_right_node(2)
tree.get_root().get_right_node().get_right_node().set_left_node(2)
tree.get_root().get_right_node().get_right_node().set_right_node(2)
tree.count_univals()
print ({tree})


