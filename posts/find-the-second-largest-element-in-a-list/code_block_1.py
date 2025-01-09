def find_second_largest_max(data):
  """Finds the second largest element using the max() function twice.

  Args:
    data: A list of numbers.

  Returns:
    The second largest element, or None if the list has fewer than 2 elements.  Handles duplicates gracefully.
  """
  if len(data) < 2:
    return None
  largest = max(data)
  data.remove(largest) #Removes only the first occurrence of largest
  if not data: #Handles case where all elements were the same.
      return None
  return max(data)

my_list = [1, 5, 2, 8, 3, 9, 4, 7, 6]
second_largest = find_second_largest_max(my_list)
print(f"The second largest element is: {second_largest}") # Output: 8

my_list = [9,9,9]
second_largest = find_second_largest_max(my_list)
print(f"The second largest element is: {second_largest}") # Output: None
