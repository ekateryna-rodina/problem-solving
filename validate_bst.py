# This is an input class. Do not edit.
import unittest
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
	if not tree:
		return True
	if tree.left:
		if not tree.value > tree.left.value:
			return False
	if tree.right:
		if not tree.value <= tree.right.value:
			return False

	return validateBst(tree.left) and validateBst(tree.right)


root = BST(10)

root.left = BST(5)
root.left.left = None
root.left.right = BST(10)
root.left.right.right = None
root.left.right.left = None

root.right = BST(15)
root.right.left = None
root.right.right = BST(22)
root.right.right.right = BST(500)
root.right.right.right.left = BST(50)
root.right.right.right.right = BST(1500)
root.right.right.right.right.left = None
root.right.right.right.right.right = BST(10000)
root.right.right.right.right.right.left = BST(2200)
root.right.right.right.right.right.right = BST(9999)
root.right.right.right.right.right.right.left = None
root.right.right.right.right.right.right.right = None


root.right.right.left = None

print(validateBst(root))


# {
#   "tree": {
#     "nodes": [
#       {"id": "10", "left": "5", "right": "15", "value": 10},
#       {"id": "15", "left": null, "right": "22", "value": 15},
#       {"id": "22", "left": null, "right": "500", "value": 22},
#       {"id": "500", "left": "50", "right": "1500", "value": 500},
#       {"id": "1500", "left": null, "right": "10000", "value": 1500},
#       {"id": "10000", "left": "2200", "right": "9999", "value": 10000},
#       {"id": "9999", "left": null, "right": null, "value": 9999},

#       {"id": "2200", "left": null, "right": null, "value": 2200},
#       {"id": "50", "left": null, "right": "200", "value": 50},
#       {"id": "200", "left": null, "right": null, "value": 200},
#       {"id": "5", "left": "2", "right": "5-2", "value": 5},
#       {"id": "5-2", "left": null, "right": null, "value": 5},
#       {"id": "2", "left": "1", "right": null, "value": 2},
#       {"id": "1", "left": null, "right": null, "value": 1}
#     ],
#     "root": "10"
#   }
# }