def linear_search(data, target):
    """Performs a linear search. O(n) complexity."""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1 # Target not found

my_list = [2, 5, 7, 8, 11, 12]
index = linear_search(my_list, 8)
print(index) #Output: 3