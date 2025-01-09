my_set = {1, 2, 3}
my_set.update([4, 5, 6])
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}
my_set.update({7,8}, {9,10}) # Update with multiple iterables
print(my_set) #Output: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}