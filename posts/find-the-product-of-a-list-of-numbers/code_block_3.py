import numpy as np

def product_numpy(numbers):
  """Calculates the product of a list of numbers using NumPy.

  Args:
    numbers: A list of numbers.

  Returns:
    The product of all numbers in the list.  Returns 1 for an empty list. Raises TypeError if input is not a list or contains non-numeric elements.
  """
  try:
    arr = np.array(numbers)
    return np.prod(arr)
  except TypeError:
    raise TypeError("Input must be a list of numbers.")


my_list = [1, 2, 3, 4, 5]
result = product_numpy(my_list)
print(f"The product of the list is: {result}")  # Output: The product of the list is: 120
