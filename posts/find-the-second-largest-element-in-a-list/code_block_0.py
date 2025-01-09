def find_second_largest_sorting(data):
  """Finds the second largest element in a list using sorting.

  Args:
    data: A list of numbers.

  Returns:
    The second largest element in the list, or None if the list has fewer than 2 elements.
  """
  if len(data) < 2:
    return None
  sorted_data = sorted(data, reverse=True)
  return sorted_data[1]

my_list = [1, 5, 2, 8, 3, 9, 4, 7, 6]
second_largest = find_second_largest_sorting(my_list)
print(f"The second largest element is: {second_largest}") # Output: 8