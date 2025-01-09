my_list = [1, 2, 2, 3, 4, 4, 5, 1]
unique_list = list(dict.fromkeys(my_list))

print(f"Original list: {my_list}")
print(f"List with duplicates removed (order might change): {unique_list}")