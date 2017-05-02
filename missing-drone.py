#using brutre force approach - O(n^2) time
#using hashset - O(n) time O(n) space
#using bitwise operation: XOR O(n) time O(1) space
#does work for more than one unique
def missing_drone(drone_numbers):
    unique = set()
    for i in drone_numbers:
        if i not in unique:
            unique.add(i)
        else:
            unique.remove(i)
    for i in unique:
        print i

drone_numbers = [1,2,3,45,65,3,1,4,45]
missing_drone(drone_numbers)
