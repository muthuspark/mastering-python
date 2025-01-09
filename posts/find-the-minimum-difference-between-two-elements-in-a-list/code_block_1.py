def min_difference_sorting(data):
  """
  Finds the minimum difference between any two elements in a list after sorting.

  Args:
    data: A list of numbers.

  Returns:
    The minimum difference between any two elements in the list. Returns infinity if the list has fewer than 2 elements.
  """
  if len(data) < 2:
    return float('inf')

  data.sort()
  min_diff = float('inf')
  for i in range(len(data) - 1):
    diff = data[i+1] - data[i]
    if diff < min_diff:
      min_diff = diff
  return min_diff

my_list = [1, 5, 3, 19, 18, 25]
min_diff = min_difference_sorting(my_list)
print(f"Minimum difference (sorting): {min_diff}") # Output: 1