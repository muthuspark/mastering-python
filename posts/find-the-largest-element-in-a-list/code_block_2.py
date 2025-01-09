def find_largest_robust(data):
  """Finds the largest element, handling empty lists and non-numeric data.

  Args:
    data: A list of numbers.

  Returns:
    The largest element in the list, or None if the list is empty or contains non-numeric data.
  """
  if not data:
    return None
  try:
    return max(data)
  except TypeError:
    return None #or raise a more specific exception

my_list = [1, 5, 2, 8, 3]
largest_element = find_largest_robust(my_list)
print(f"The largest element is: {largest_element}") # Output: The largest element is: 8

my_list = []
largest_element = find_largest_robust(my_list)
print(f"The largest element is: {largest_element}") # Output: The largest element is: None

my_list = [1, "a", 2, 3]
largest_element = find_largest_robust(my_list)
print(f"The largest element is: {largest_element}") # Output: The largest element is: None