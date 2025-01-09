def is_subset_set(list1, list2):
  """
  Checks if list1 is a subset of list2 using sets.

  Args:
    list1: The potential subset list.
    list2: The larger list to check against.

  Returns:
    True if list1 is a subset of list2, False otherwise.
  """
  set1 = set(list1)
  set2 = set(list2)
  return set1.issubset(set2)

list_a = [1, 2, 3]
list_b = [1, 2, 3, 4, 5]
list_c = [1, 6, 7]

print(f"Is {list_a} a subset of {list_b}? {is_subset_set(list_a, list_b)}") # Output: True
print(f"Is {list_c} a subset of {list_b}? {is_subset_set(list_c, list_b)}") # Output: False
