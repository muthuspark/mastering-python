my_list = [10, 20, 30, 40, 50]
sliced_list = my_list[1:4]
sliced_list[0] = 99  # Modify the sliced list

print(f"Original list: {my_list}")      # Output: Original list: [10, 20, 30, 40, 50]
print(f"Modified sliced list: {sliced_list}") # Output: Modified sliced list: [99, 30, 40]