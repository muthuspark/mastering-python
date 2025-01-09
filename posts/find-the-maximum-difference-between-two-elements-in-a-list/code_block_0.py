def max_difference_bruteforce(data):
  """Finds the maximum difference between two elements in a list using brute force.

  Args:
    data: A list of numbers.

  Returns:
    The maximum difference between any two elements in the list, or 0 if the list 
    has fewer than two elements.  Returns None if the input is not a list or contains non-numeric values.
  """
  if not isinstance(data, list):
    return None
  if len(data) < 2:
    return 0
  if not all(isinstance(x, (int, float)) for x in data):
    return None

  max_diff = 0
  for i in range(len(data)):
    for j in range(i + 1, len(data)):
      diff = abs(data[i] - data[j])
      max_diff = max(max_diff, diff)
  return max_diff

my_list = [7, 1, 5, 9, 2]
max_diff = max_difference_bruteforce(my_list)
print(f"Maximum difference (brute force): {max_diff}") # Output: 8

my_list = [1,1,1]
max_diff = max_difference_bruteforce(my_list)
print(f"Maximum difference (brute force): {max_diff}") # Output: 0

my_list = "abc"
max_diff = max_difference_bruteforce(my_list)
print(f"Maximum difference (brute force): {max_diff}") # Output: None

my_list = [1,2,"a"]
max_diff = max_difference_bruteforce(my_list)
print(f"Maximum difference (brute force): {max_diff}") # Output: None