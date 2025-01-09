def min_difference_pythonic(data):
  """
  Finds the minimum difference using min() and a generator expression.

  Args:
    data: A list of numbers.

  Returns:
    The minimum difference between any two elements in the list. Returns infinity if the list has fewer than 2 elements.
  """
  if len(data) < 2:
    return float('inf')
  data.sort()
  return min(b - a for a, b in zip(data, data[1:]))

#Example Usage
my_list = [1, 5, 3, 19, 18, 25]
min_diff = min_difference_pythonic(my_list)
print(f"Minimum difference (Pythonic): {min_diff}") # Output: 1
