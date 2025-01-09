my_set.remove(3) # Raises KeyError if element not found
print(my_set)  # Output: {1, 2, 4, 5, 6, 7}

my_set.discard(8) #Does not raise error if element not found
print(my_set) # Output: {1, 2, 4, 5, 6, 7}

removed_element = my_set.pop() #Removes and returns an arbitrary element
print(removed_element) #Output: 1 (or any other element)
print(my_set) #Output: {2, 4, 5, 6, 7}

my_set.clear() #Removes all elements
print(my_set) #Output: set()