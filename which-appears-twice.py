#1: out of place approach
#2: using math
def which_appears_twice(list_of_integers):
    new_list = []
    for item in list_of_integers:
        if item not in new_list:
            new_list.append(item)
        else:
            return item
def which_appears_twice_math(list_of_integers, list_of_integers_with_repeated_number):
    res = sum(list_of_integers)
    res2 = sum(list_of_integers_with_repeated_number)
    return res2 - res

list_of_integers = [1,13,15,17,19,4,33]
list_of_integers_with_repeated_number = [1,13,15,17,19,4,33,33]
print "Using Out of Place approach: ", which_appears_twice(list_of_integers_with_repeated_number)
print "Using math: ", which_appears_twice_math(list_of_integers, list_of_integers_with_repeated_number)
