import math

def binary_search(data, target):
    """Performs a binary search. O(log n) complexity."""
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # Target not found

sorted_data = [2, 5, 7, 8, 11, 12]
index = binary_search(sorted_data, 11)
print(index) # Output: 4
