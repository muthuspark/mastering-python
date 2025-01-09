list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

symmetric_difference = set(list1) ^ set(list2) #Elements unique to either list
print(f"Symmetric difference: {symmetric_difference}") # Output: Symmetric difference: {1, 2, 4, 6, 7, 8}

symmetric_difference = list(symmetric_difference) #Convert back to list if needed
print(f"Symmetric difference (list): {symmetric_difference}") # Output: Symmetric difference (list): [1, 2, 4, 6, 7, 8]