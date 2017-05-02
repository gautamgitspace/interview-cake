from Stack import *
class Parenthesis:
    def __init__(self):
        self.base = Stack()
    def push(self, item):
        self.base.push(item)
    def pop(self):
        val = self.base.pop()
        return val
s = Parenthesis()
test_input_1 = "(this(here) can be useful(helpful(valuable)))"
test_opening_1 = 5
#use test case 2 to ruin balancing
test_input_2 = "(this(here) can be useful(helpful(valuable))"
test_opening_2 = 0
not_found = False
d = {}
for i, item in enumerate(test_input_1):
    if item == "(":
        s.push(i)
    if item == ")":
        d[s.pop()] = i
for key, value in d.items():
    print key, value
for key, value in d.items():
    if key == test_opening_1:
        print "closing found at: ", value
    if test_opening_1 not in d.keys():
        not_found = True
if not_found:
    print "No Closing Parenthesis found for the specified Opening"
