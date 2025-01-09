from collections import Counter

def is_unique_counter(data):
  """
  Checks if a list contains only unique elements using Counter.

  Args:
    data: A list of elements.

  Returns:
    True if the list contains only unique elements, False otherwise.
  """
  counts = Counter(data)
  return all(count == 1 for count in counts.values())

#Example Usage
my_list = [1, 2, 3, 4, 5]
print(f"List {my_list} contains only unique elements: {is_unique_counter(my_list)}")  # Output: True

my_list = [1, 2, 3, 4, 5, 1]
print(f"List {my_list} contains only unique elements: {is_unique_counter(my_list)}")  # Output: False