"""
Write a function get_products_of_all_ints_except_at_index()
that takes a list of integers and returns a list of the products.
for each index you want to find the product of every integer
except the integer at that index.
"""
def get_products_of_all_ints_except_at_index(list_of_numbers):
    resultant_array = [1] * len(list_of_numbers)
    product = 1
    for i in range(len(list_of_numbers)):
        resultant_array[i]=product
        product*=list_of_numbers[i]
    product = 1
    for i in range(len(list_of_numbers)-1, 0, -1):
        resultant_array[i]*=product
        product*=list_of_numbers[i]
    resultant_array[0]=product
    return resultant_array
list_of_numbers = [1,2,3,4,1,2]
result = get_products_of_all_ints_except_at_index(list_of_numbers)
print result
