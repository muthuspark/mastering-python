def list_length_recursive(data):
  """
  Calculates the length of a list using recursion.

  Args:
    data: The input list.

  Returns:
    The length of the list.
  """
  if not data:
    return 0
  else:
    return 1 + list_length_recursive(data[1:])

my_list = [10, 20, 30, 40, 50]
length = list_length_recursive(my_list)
print(f"The length of the list is: {length}")  # Output: The length of the list is: 5