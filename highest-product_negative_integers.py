"""
Keep track of the highest_product_of_2 and lowest_product_of_2(could be a low negative number).
If the current number times one of those is higher than the current highest_product_of_three,
we have a new highest_product_of_three!

So at each iteration we're keeping track of and updating:

highest_product_of_three
highest_product_of_2
highest
lowest_product_of_2
lowest
"""

def highest_product(arr):
    highest = max(arr[0], arr[1])
    print 'HIGHEST', highest
    lowest = min(arr[0], arr[1])
    print 'LOWEST', lowest
    highest_product_of_two = highest * lowest
    lowest_product_of_two = highest * lowest
    print 'H_O_T', highest_product_of_two
    print 'L_O_T', lowest_product_of_two
    max_product = highest_product_of_two * arr[2]
    print 'MP', max_product

    for elem in arr:
        max_product = max( max_product, elem * highest_product_of_two, elem * lowest_product_of_two )
        highest_product_of_two = max( highest_product_of_two, elem * highest, elem * lowest )
        lowest_product_of_two = min( lowest_product_of_two, elem * highest, elem * lowest )
        highest = max( highest, elem)
        lowest = min( lowest, elem)
    return max_product

list_of_numbers = [-1,3,9,6,9,-99,-1]
result = highest_product(list_of_numbers)
print result
