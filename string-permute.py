#range returns a Python list object and xrange returns an xrange object.
#xrange doesn't actually generate a static list at run-time like range does.
#It creates the values as you need them with a special technique called yielding
def permute(input, starting_index, ending_index):
    if starting_index==ending_index:
        print ''.join(input)
    else:
        for i in xrange(starting_index,ending_index+1):
            input[starting_index], input[i] = input[i], input[starting_index]
            permute(input, starting_index+1, ending_index)
            input[starting_index], input[i] = input[i], input[starting_index]

string = "SUNY"
length = len(string)
input = list(string)
#list, starting index, ending index
permute(input, 0, length-1)
