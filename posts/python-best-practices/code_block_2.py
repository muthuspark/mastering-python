def calculate_average(numbers):
  """Calculates the average of a list of numbers.

  Args:
    numbers: A list of numerical values.

  Returns:
    The average of the numbers. Returns 0 if the list is empty.
  """
  if not numbers:
    return 0
  return sum(numbers) / len(numbers)

help(calculate_average)