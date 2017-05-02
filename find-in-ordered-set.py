#Suppose we had an array of n integers in sorted order.
#How quickly could we check if a given integer is in the array?
#This is the classical Binary Search Problem. This can be done in O(Log n)
#using iteration
def find(list_of_integers, x):
    ceiling = len(list_of_integers)
    floor = -1
    while floor+1 < ceiling:
        d = ceiling - floor
        half_distance = d/2
        mid = floor + half_distance
        if list_of_integers[mid] == x:
            return True
        if list_of_integers[mid] > x:
            ceiling = mid
        else:
            floor = mid
    return False


list_of_integers = [10,29,39,46,57,63,78]
x = 67
print "exists:",find(list_of_integers,x)
