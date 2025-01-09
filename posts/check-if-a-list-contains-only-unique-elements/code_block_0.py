def is_unique_set(data):
  """
  Checks if a list contains only unique elements using sets.

  Args:
    data: A list of elements.

  Returns:
    True if the list contains only unique elements, False otherwise.
  """
  return len(data) == len(set(data))

#Example Usage
my_list = [1, 2, 3, 4, 5]
print(f"List {my_list} contains only unique elements: {is_unique_set(my_list)}")  # Output: True

my_list = [1, 2, 3, 4, 5, 1]
print(f"List {my_list} contains only unique elements: {is_unique_set(my_list)}")  # Output: False