def is_subset_generator(list1, list2):
    return all(x in list2 for x in list1)

#Example Usage (same output as above)
list_a = [1, 2, 3]
list_b = [1, 2, 3, 4, 5]
list_c = [1, 6, 7]

print(f"Is {list_a} a subset of {list_b}? {is_subset_generator(list_a, list_b)}")
print(f"Is {list_c} a subset of {list_b}? {is_subset_generator(list_c, list_b)}")