def is_sorted_iterative(data):
  """Checks if a list is sorted in ascending order using iteration.

  Args:
    data: The list to check.

  Returns:
    True if the list is sorted in ascending order, False otherwise.
  """
  for i in range(len(data) - 1):
    if data[i] > data[i+1]:
      return False
  return True

my_list = [1, 2, 3, 4, 5]
print(f"Is {my_list} sorted? {is_sorted_iterative(my_list)}")  # Output: True

my_list = [1, 3, 2, 4, 5]
print(f"Is {my_list} sorted? {is_sorted_iterative(my_list)}")  # Output: False

my_list = [] #Handle empty list case
print(f"Is {my_list} sorted? {is_sorted_iterative(my_list)}")  # Output: True

my_list = [5] #Handle single element list case
print(f"Is {my_list} sorted? {is_sorted_iterative(my_list)}")  # Output: True