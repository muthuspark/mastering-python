list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

union_list = list(set(list1 + list2)) #Combine lists then use set for uniqueness

print(f"Union as a list: {union_list}")

#Output:
#Union as a list: [1, 2, 3, 4, 5, 6, 7, 8]