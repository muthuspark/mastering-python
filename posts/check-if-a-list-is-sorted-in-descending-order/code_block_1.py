def is_sorted_descending_all(data):
  """Checks if a list is sorted in descending order using all() and zip().

  Args:
    data: The input list.

  Returns:
    True if the list is sorted in descending order, False otherwise.
  """
  return all(data[i] >= data[i+1] for i in range(len(data)-1))


my_list = [9, 7, 5, 3, 1]
print(f"Is {my_list} sorted descending (all/zip)? {is_sorted_descending_all(my_list)}")  # Output: True

my_list = [9, 7, 10, 3, 1]
print(f"Is {my_list} sorted descending (all/zip)? {is_sorted_descending_all(my_list)}")  # Output: False

my_list = []
print(f"Is {my_list} sorted descending (all/zip)? {is_sorted_descending_all(my_list)}")  # Output: True

my_list = [5]
print(f"Is {my_list} sorted descending (all/zip)? {is_sorted_descending_all(my_list)}")  # Output: True