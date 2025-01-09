list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

union_set = set1.union(set2)
union_list = list(union_set)

print(f"Union as a set: {union_set}")
print(f"Union as a list: {union_list}")

#Output:
#Union as a set: {1, 2, 3, 4, 5, 6, 7, 8}
#Union as a list: [1, 2, 3, 4, 5, 6, 7, 8]