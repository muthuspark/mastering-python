my_list = [1, 2, 3]

my_list.append(4)       # Add to the end
my_list.insert(1, 1.5)  # Insert at a specific index
my_list.extend([5, 6]) # Add multiple elements at the end

my_list.remove(2)       # Remove the first occurrence of 2
del my_list[0]         # Remove element at index 0
popped_element = my_list.pop() # Remove and return the last element


print(my_list)  # Output: [1.5, 3, 4, 5, 6]
print(popped_element) # Output: 6