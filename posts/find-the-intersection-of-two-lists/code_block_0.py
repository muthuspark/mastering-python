list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

intersection = set1.intersection(set2)  # or set1 & set2

print(f"The intersection of the two lists is: {list(intersection)}") #Convert back to list for output