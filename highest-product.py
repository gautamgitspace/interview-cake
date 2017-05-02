"""
Given a list_of_ints, find the highest_product you can get from three of the
integers.The input list_of_ints will always have at least three integers.
"""
#works for positive integers

def highest_product(list_of_numbers):
    if len(list_of_numbers)<3:
        print 'You gotta be kidding me'
        exit()
    if len(list_of_numbers)==3:
        return list_of_numbers[0]*list_of_numbers[1]*list_of_numbers[2]
    max1 = max2 = max3 = None
    for item in list_of_numbers:
        if max1 == None or max1<item:
            max1=item
    list_of_numbers.pop(list_of_numbers.index(max1))

    for item in list_of_numbers:
        if max2 == None or max2<item:
            max2=item
    list_of_numbers.pop(list_of_numbers.index(max2))

    for item in list_of_numbers:
        if max3 == None or max3<item:
            max3=item
    list_of_numbers.pop(list_of_numbers.index(max3))

    return max1*max2*max3
list_of_numbers = [1,3,9,6,9]
result = highest_product(list_of_numbers)
print result
