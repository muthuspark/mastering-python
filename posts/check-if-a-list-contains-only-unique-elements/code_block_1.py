def is_unique_loop(data):
  """
  Checks if a list contains only unique elements using a loop and a dictionary.

  Args:
    data: A list of elements.

  Returns:
    True if the list contains only unique elements, False otherwise.
  """
  seen = {} #or seen = [] for list implementation
  for item in data:
    if item in seen:
      return False
    seen[item] = True #or seen.append(item) for list implementation
  return True


#Example Usage
my_list = [1, 2, 3, 4, 5]
print(f"List {my_list} contains only unique elements: {is_unique_loop(my_list)}")  # Output: True

my_list = [1, 2, 3, 4, 5, 1]
print(f"List {my_list} contains only unique elements: {is_unique_loop(my_list)}")  # Output: False