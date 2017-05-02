#using bitwise operation: XOR O(n) time O(1) space
#returns only one unique integer. does not work for more than one.
def missing_drone(drone_numbers):
    unique_drone_id = 0
    for id in drone_numbers:
        unique_drone_id ^= id
    return unique_drone_id
drone_numbers = [1,2,3,45,65,65,45,4,4,3,2]
print missing_drone(drone_numbers)
