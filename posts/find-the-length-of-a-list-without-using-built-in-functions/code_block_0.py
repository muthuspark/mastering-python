def list_length_iterative(data):
  """
  Calculates the length of a list using iteration.

  Args:
    data: The input list.

  Returns:
    The length of the list.
  """
  count = 0
  for _ in data:  # Underscore indicates we don't need the element's value
    count += 1
  return count

my_list = [1, 2, 3, 4, 5]
length = list_length_iterative(my_list)
print(f"The length of the list is: {length}")  # Output: The length of the list is: 5