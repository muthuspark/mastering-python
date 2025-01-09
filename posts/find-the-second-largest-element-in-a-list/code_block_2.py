def find_second_largest_iterative(data):
  """Finds the second largest element using a single pass iterative approach.

  Args:
    data: A list of numbers.

  Returns:
    The second largest element, or None if the list has fewer than 2 elements. Handles duplicates.
  """
  if len(data) < 2:
    return None
  largest = float('-inf')
  second_largest = float('-inf')
  for num in data:
    if num > largest:
      second_largest = largest
      largest = num
    elif num > second_largest and num != largest:
      second_largest = num
  if second_largest == float('-inf'):
      return None
  return second_largest

my_list = [1, 5, 2, 8, 3, 9, 4, 7, 6]
second_largest = find_second_largest_iterative(my_list)
print(f"The second largest element is: {second_largest}")  # Output: 8

my_list = [9,9,9]
second_largest = find_second_largest_iterative(my_list)
print(f"The second largest element is: {second_largest}")  # Output: None