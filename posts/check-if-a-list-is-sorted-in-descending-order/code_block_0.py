def is_sorted_descending_loop(data):
  """Checks if a list is sorted in descending order using a loop.

  Args:
    data: The input list.

  Returns:
    True if the list is sorted in descending order, False otherwise.
  """
  for i in range(len(data) - 1):
    if data[i] < data[i+1]:
      return False
  return True

my_list = [9, 7, 5, 3, 1]
print(f"Is {my_list} sorted descending (loop)? {is_sorted_descending_loop(my_list)}")  # Output: True

my_list = [9, 7, 10, 3, 1]
print(f"Is {my_list} sorted descending (loop)? {is_sorted_descending_loop(my_list)}")  # Output: False

my_list = []
print(f"Is {my_list} sorted descending (loop)? {is_sorted_descending_loop(my_list)}")  # Output: True (empty list considered sorted)

my_list = [5]
print(f"Is {my_list} sorted descending (loop)? {is_sorted_descending_loop(my_list)}")  # Output: True (single-element list considered sorted)