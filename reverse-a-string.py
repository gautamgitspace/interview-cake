#In Python, strings are immutable. Changing a string does not
#modify the string. It creates a new one. Hence no point of doing
#it in place.
#APPROACH 1: def reverse
#APPROACH 2: def reverse_using_chars
def reverse(input):
    #This is extended slice syntax. It works by doing [begin:end:step]
    return input[::-1]

def reverse_using_chars(input):
    length = len(input)
    reverse_str = []
    while length > 0:
        reverse_str.append(input[length-1])
        length-=1
    return "".join(reverse_str)

input = raw_input("Enter a string: ")
print "Using PYTHONIC APPROACH: ", reverse(input)
print "Using char by char approach:", reverse_using_chars(input)
