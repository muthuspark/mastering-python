my_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = [item for i, item in enumerate(my_list) if item not in my_list[:i]]

print(f"Original list: {my_list}")
print(f"List with duplicates removed (order preserved): {unique_list}")