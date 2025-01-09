list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

common_elements = [x for x in list1 if x in list2]
print(f"Common elements using list comprehension: {common_elements}")