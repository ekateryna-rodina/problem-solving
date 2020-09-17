tree = {'value': 10, 
        'left': {'value': 5, 
                'left': {'value': 2, 
                        'left': {'value': 1, 
                                'left': None, 
                                'right': None}, 
                        'right': None
                        }, 
                'right': {'value': 5, 
                        'left': None, 
                        'right': None}
                }, 
        'right': {'value': 15, 
                'left':None, 
                'right': {'value': 22,
                          'left': None,
                          'right': None
                          }
                }
        }
print(tree)

def inOrderTraverse(tree, array):
    if not tree:
        return
    inOrderTraverse(tree['left'], array)
    array.append(tree['value'])
    inOrderTraverse(tree['right'], array)
    return array
	
def preOrderTraverse(tree, array):
    if not tree:
        return 
    array.append(tree['value'])
    preOrderTraverse(tree['left'], array)
    preOrderTraverse(tree['right'], array)
    return array

def postOrderTraverse(tree, array):
    if not tree:
        return 

    postOrderTraverse(tree['left'], array)
    postOrderTraverse(tree['right'], array)
    array.append(tree['value'])
    return array

# print(inOrderTraverse(tree, []))
print(preOrderTraverse(tree, []))
# print(postOrderTraverse(tree, []))