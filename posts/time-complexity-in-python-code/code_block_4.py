def bubble_sort(data):
    """Performs a bubble sort. O(n^2) complexity."""
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

my_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(my_list)
print(sorted_list) # Output: [11, 12, 22, 25, 34, 64, 90]