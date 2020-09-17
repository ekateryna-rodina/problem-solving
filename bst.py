# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while True:
            if value < current.value:
                if not current.left:
                    current.left = BST(value)
                    break
                current = current.left
            else:
                if not current.right:
                    current.right = BST(value)
                    break
                current = current.right
        return self

    def contains(self, value):
        current = self
        while current:
            if value < current.value:
                current = current.left
            elif value > current.value:
                current = current.right
            else:
                return True

        return False

    def remove(self, value, parentNode = None):
        # track root node tto connect nodes if necessary
        current = self
        while current:
            if value < current.value:
                parentNode = current
                current = current.left
            elif value > current.value:
                parentNode = current
                current = current.right
            else:
                # if the node does have children
                if current.left and current.right:
                    current.value = current.right.get_min_value()
                    current.rigth.remove(current.value, current)
                # if the node is a root node
                elif not parentNode:
                    # if root has left node
                    if current.left:
                        current.value = current.left.value
                        current.left = current.left.left
                        current.right = current.left.right
                    # if root has right node
                    elif current.right:
                        current.value = current.right.value
                        current.left = current.right.left
                        current.right = current.right.right
                    # if root does not have children
                    else:
                        current.value = None
                # if the node to delete is a child
                elif parentNode.left == parentNode:
                    parentNode.left = current.left if current.left else current.right
                elif parentNode.right == parentNode:
                    parentNode.right = current.rigth if current.right else current.left
                break
        return self
# because we want to replace it to minimum vvalue so we search left
def get_min_value(self):
    current = self
    while self.left:
        current = self.left
    return current

tree = BST(5)
tree.insert(6)
tree.insert(8)
tree.insert(10)
tree.insert(3)
tree.insert(2)
print(tree.contains(6))
print(tree.contains(10))
print(tree.contains(2))
print(tree.contains(7))
print(tree.contains(9))
tree.remove(10)