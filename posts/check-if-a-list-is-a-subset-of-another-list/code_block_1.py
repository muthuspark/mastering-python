def is_subset_list_comprehension(list1, list2):
  """
  Checks if list1 is a subset of list2 using list comprehension.

  Args:
    list1: The potential subset list.
    list2: The larger list to check against.

  Returns:
    True if list1 is a subset of list2, False otherwise.
  """
  return all(item in list2 for item in list1)

list_a = [1, 2, 3]
list_b = [1, 2, 3, 4, 5]
list_c = [1, 6, 7]

print(f"Is {list_a} a subset of {list_b}? {is_subset_list_comprehension(list_a, list_b)}")
print(f"Is {list_c} a subset of {list_b}? {is_subset_list_comprehension(list_c, list_b)}")