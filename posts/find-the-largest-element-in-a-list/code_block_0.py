def find_largest_loop(data):
  """Finds the largest element in a list using a loop.

  Args:
    data: A list of numbers.

  Returns:
    The largest element in the list, or None if the list is empty.
  """
  if not data:
    return None
  largest = data[0]  # Initialize with the first element
  for element in data:
    if element > largest:
      largest = element
  return largest

my_list = [1, 5, 2, 8, 3]
largest_element = find_largest_loop(my_list)
print(f"The largest element is: {largest_element}") # Output: The largest element is: 8