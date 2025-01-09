list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

difference = set(list1) - set(list2)  # Elements in list1 but not in list2
print(f"Elements unique to list1: {difference}") # Output: Elements unique to list1: {1, 2, 4}

difference = list(difference) #Convert back to list if needed
print(f"Elements unique to list1 (list): {difference}") # Output: Elements unique to list1 (list): [1, 2, 4]