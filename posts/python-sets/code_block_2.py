set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1 | set2  # Using the pipe operator
print(union_set)  # Output: {1, 2, 3, 4, 5}

union_set = set1.union(set2) # Using the union() method
print(union_set) # Output: {1, 2, 3, 4, 5}