def calculate_mean(numbers):
  """Calculates the mean of a list of numbers.

  Args:
    numbers: A list of numbers.

  Returns:
    The mean of the numbers, or None if the list is empty.
  """
  if not numbers:
    return None  # Handle empty list case
  total = sum(numbers)
  mean = total / len(numbers)
  return mean

my_list = [10, 20, 30, 40, 50]
mean = calculate_mean(my_list)
print(f"The mean of {my_list} is: {mean}") # Output: The mean of [10, 20, 30, 40, 50] is: 30.0