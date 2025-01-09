set1 = {1, 2, 3}
set2 = {3, 4, 5}

difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}

difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}

difference_set = set2 - set1
print(difference_set) # Output: {4, 5}