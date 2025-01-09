my_list = [10, 20, 30, 40, 50]

sliced_list = my_list[-3:]
print(f"Last three elements: {sliced_list}")  # Output: Last three elements: [30, 40, 50]

sliced_list = my_list[::-2]
print(f"Every other element from the end: {sliced_list}") # Output: Every other element from the end: [50, 30, 10]
