def max_difference_efficient(data):
  """Finds the maximum difference between two elements in a list efficiently.

  Args:
    data: A list of numbers.

  Returns:
    The maximum difference between any two elements in the list, or 0 if the list 
    has fewer than two elements. Returns None if the input is not a list or contains non-numeric values.
  """
  if not isinstance(data, list):
    return None
  if len(data) < 2:
    return 0
  if not all(isinstance(x, (int, float)) for x in data):
    return None

  min_val = data[0]
  max_val = data[0]
  for x in data:
    min_val = min(min_val, x)
    max_val = max(max_val, x)
  return max_val - min_val

my_list = [7, 1, 5, 9, 2]
max_diff = max_difference_efficient(my_list)
print(f"Maximum difference (efficient): {max_diff}") # Output: 8

my_list = [1,1,1]
max_diff = max_difference_efficient(my_list)
print(f"Maximum difference (efficient): {max_diff}") # Output: 0

my_list = "abc"
max_diff = max_difference_efficient(my_list)
print(f"Maximum difference (efficient): {max_diff}") # Output: None

my_list = [1,2,"a"]
max_diff = max_difference_efficient(my_list)
print(f"Maximum difference (efficient): {max_diff}") # Output: None