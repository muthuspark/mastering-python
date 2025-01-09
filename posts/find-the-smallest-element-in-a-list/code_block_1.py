my_list = [3, 1, 4, 1, 5, 9, 2, 6]
smallest_element = my_list[0]  # Initialize with the first element

for element in my_list:
    if element < smallest_element:
        smallest_element = element

print(f"The smallest element is: {smallest_element}")  # Output: The smallest element is: 1