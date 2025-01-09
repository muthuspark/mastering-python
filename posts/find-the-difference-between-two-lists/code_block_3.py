list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

difference = list(filter(lambda x: x not in list2, list1))
print(f"Elements unique to list1: {difference}") # Output: Elements unique to list1: [1, 2, 4]