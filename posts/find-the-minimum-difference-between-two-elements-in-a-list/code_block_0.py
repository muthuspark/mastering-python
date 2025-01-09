def min_difference_brute_force(data):
  """
  Finds the minimum difference between any two elements in a list using brute force.

  Args:
    data: A list of numbers.

  Returns:
    The minimum difference between any two elements in the list.  Returns infinity if the list has fewer than 2 elements.
  """
  if len(data) < 2:
    return float('inf')  # Return infinity for lists with less than 2 elements

  min_diff = float('inf')
  for i in range(len(data)):
    for j in range(i + 1, len(data)):
      diff = abs(data[i] - data[j])
      if diff < min_diff:
        min_diff = diff
  return min_diff

my_list = [1, 5, 3, 19, 18, 25]
min_diff = min_difference_brute_force(my_list)
print(f"Minimum difference (brute force): {min_diff}") # Output: 1