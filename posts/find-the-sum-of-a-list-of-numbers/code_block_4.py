nested_list = [[1, 2, 3], [4, 5], [6]]
total = sum(sum(inner_list) for inner_list in nested_list)
print(f"The sum is: {total}") # Output: The sum is: 21