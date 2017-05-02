# simply walk through the stack and find the max element.
#This takes O(n) time for each call to get_max()
from Stack import *
class MaxStack:
     def __init__(self):
         self.base = Stack()
         self.max = Stack()
     def push(self, item):
        if item >= self.max.peek():
            self.max.push(item)
        self.base.push(item)
     def pop(self):
         val = self.base.pop()
         if (val == self.max.peek()):
             self.max.pop()
         return val
     def getmax(self):
         return self.max.peek()


s=MaxStack()

s.push(45)
s.push(35)
s.push(65)
max1 = s.getmax()
print "max after pushing 45,35 and 65: ", max1
s.push(87)
max2 = s.getmax()
print "max after pushing 87 now: ", max2
print "POPPING CHERRY", (s.pop())
print"POPPING CHERRY", (s.pop())
max3 = s.getmax()
print "max after popping 2 elements: ", max3
