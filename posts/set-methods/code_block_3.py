my_set = {1, 2, 3, 4}
my_set.discard(3)
print(my_set)  # Output: {1, 2, 4}
my_set.discard(5)  # No error is raised
print(my_set)  # Output: {1, 2, 4}