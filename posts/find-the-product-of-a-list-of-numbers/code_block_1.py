from functools import reduce
import operator

def product_reduce(numbers):
  """Calculates the product of a list of numbers using functools.reduce.

  Args:
    numbers: A list of numbers.

  Returns:
    The product of all numbers in the list. Returns 1 if the list is empty.
  """
  if not numbers:
    return 1
  return reduce(operator.mul, numbers)

my_list = [1, 2, 3, 4, 5]
result = product_reduce(my_list)
print(f"The product of the list is: {result}")  # Output: The product of the list is: 120