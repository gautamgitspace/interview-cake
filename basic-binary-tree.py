class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
    def insert(self, data):
        #if data already exists - DO NOT insert
        #if data at root greater than data, insert at left
        #if data at root smaller than data, insert at right
        if self.value == data:
            return False
        elif self.value > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = Node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = Node(data)
                return True
    def delete(self, data):
        #CASE 1 : if the node has no children, kill it!
        #CASE 2 : if the node has one child/sub-tree, make the parent point to that child/sub-tree
        #CASE 3 : if the node has two children, find max in left sub-tree OR find min in right sub-tree
                
    def find(self, data):
        if self.value == data:
            return True
        elif self.value > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False
    def preOrder(self):
        if self:
            print self.value
            if self.left:
                self.left.preOrder()
            if self.right:
                self.right.preOrder()
    def inOrder(self):
        if self:
            if self.left:
                self.left.inOrder()
            print self.value
            if self.right:
                self.right.inOrder()
    def postOrder(self):
        if self:
            if self.left:
                self.left.postOrder()
            if self.right:
                self.right.postOrder()
            print self.value

class Tree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    def preOrder(self):
        if self.root:
            print "PRE-ORDER"
            self.root.preOrder()
    def inOrder(self):
        if self.root:
            print "IN-ORDER"
            self.root.inOrder()
    def postOrder(self):
        if self.root:
            print "POST-ORDER"
            self.root.postOrder()

obj = Tree()
print "INSERTION:", obj.insert(7)
print "INSERTION:", obj.insert(2)
print "INSERTION:", obj.insert(6)
print "INSERTION:", obj.insert(4)
print "INSERTION:", obj.insert(5)
print "INSERTION:", obj.insert(1)
print "INSERTION:", obj.insert(9)
print "INSERTION:", obj.insert(10)
print "INSERTION:", obj.insert(8)
print "INSERTION:", obj.insert(3)
obj.preOrder()
obj.postOrder()
obj.inOrder()
print "Element found:", obj.find(28)
print "Element found:", obj.find(20)
