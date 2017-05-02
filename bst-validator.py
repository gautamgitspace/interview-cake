#DFS more space efficient than BFS as tree's breadth grows at each level
#Both DFS and BFS will take same time O(n)
class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def tree_max(node):
    if not node:
        return float("-inf")
    maxleft  = tree_max(node.left)
    maxright = tree_max(node.right)
    print 'NODE:', node.key
    print 'MAX_RIGHT:', maxright
    print 'MAX_LEFT:', maxleft
    print 'MAX:', max(node.key, maxleft, maxright)
    return max(node.key, maxleft, maxright)

def tree_min(node):
    if not node:
        return float("inf")
    minleft  = tree_min(node.left)
    minright = tree_min(node.right)
    print 'NODE:', node.key
    print 'MIN_RIGHT', minright
    print 'MIN_LEFT', minleft
    print 'MIN:', min(node.key, minleft, minright)
    return min(node.key, minleft, minright)

def verify(node):
    if not node:
        return True
    if (tree_max(node.left) <= node.key <= tree_min(node.right) and
        verify(node.left) and verify(node.right)):
        return True
    else:
        return False

root= Node(10)
root.left = Node(5)
root.right= Node(30)
root.left.right = Node(7)
root.left.left = Node(4)
root.left.left.left = Node(2)
root.left.left.right = Node(6)
print(verify(root)) # prints FALSE, since 6 is to the left of 5

# root = Node(10)
# root.right = Node(20)
# root.left = Node(5)
# root.left.right = Node(7)
# print(verify(root)) # prints False, since 15 is to the left of 10
