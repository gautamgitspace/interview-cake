class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
def largest(node):
    if node.right:
        return largest(node.right)
    return node.value
def second_largest(node):
    #CASE 1: when we are at largest and largest element has a left-subtree
    #we will be at the largest when the node has no right sub-tree(but may have left)	
    if node.left and not node.right:
        return largest(node.left)
    #CASE 2: when we are at parent of largest and largest has no left or right tree
    if node.right and not node.right.right and not node.right.left:
        return node.value
    #otherwise keep going right
    return second_largest(node.right)

#driver CASE 2:
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.right = Node(12)
root.right.left = Node(7)
root.right.right.left = Node(10)
root.right.right.left.left = Node(9)
root.right.right.left.right = Node(11)
print second_largest(root)
