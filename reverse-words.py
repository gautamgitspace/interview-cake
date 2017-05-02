#In Python, strings are immutable. Changing a string does not
#modify the string. It creates a new one. Hence no point of doing
#it in place.
#APPROACH : def reverse_words: split the string to get a list. Perform
#in place list reversal by extended slice 
def reverse_words(input):
    result = " ".join(input.split()[::-1])
    return result


input = raw_input("Enter a string: ")
print "Using char by char approach:", reverse_using_chars(input)
