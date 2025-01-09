my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

sliced_list = my_list[2:5] 
print(f"Sliced list: {sliced_list}")  # Output: Sliced list: [30, 40, 50]

sliced_list = my_list[:4]
print(f"Sliced list: {sliced_list}")  # Output: Sliced list: [10, 20, 30, 40]

sliced_list = my_list[6:]
print(f"Sliced list: {sliced_list}")  # Output: Sliced list: [70, 80, 90, 100]

sliced_list = my_list[::2]
print(f"Sliced list: {sliced_list}")  # Output: Sliced list: [10, 30, 50, 70, 90]

reversed_list = my_list[::-1]
print(f"Reversed list: {reversed_list}") # Output: Reversed list: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]