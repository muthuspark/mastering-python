list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

common_elements = set(list1) & set(list2)  # Using the & operator for intersection
print(f"Common elements using sets: {list(common_elements)}") #Convert back to list for printing

common_elements = set(list1).intersection(list2) #Using intersection method
print(f"Common elements using intersection method: {list(common_elements)}")