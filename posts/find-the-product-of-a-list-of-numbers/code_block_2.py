from functools import reduce
import operator

def product_robust(numbers):
  """Calculates the product of a list, handling zeros and empty lists.

  Args:
    numbers: A list of numbers.

  Returns:
    The product of all numbers in the list.  Returns 1 for an empty list, 0 if a zero is present.
  """
  if not numbers:
      return 1
  if 0 in numbers:
      return 0
  return reduce(operator.mul, numbers)

my_list = [1, 2, 3, 4, 0, 5]
result = product_robust(my_list)
print(f"The product of the list is: {result}") # Output: The product of the list is: 0

my_empty_list = []
result = product_robust(my_empty_list)
print(f"The product of the empty list is: {result}") # Output: The product of the empty list is: 1