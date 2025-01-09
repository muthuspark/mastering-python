def product_loop(numbers):
  """Calculates the product of a list of numbers using a loop.

  Args:
    numbers: A list of numbers.

  Returns:
    The product of all numbers in the list. Returns 1 if the list is empty.
  """
  product = 1
  for number in numbers:
    product *= number
  return product

my_list = [1, 2, 3, 4, 5]
result = product_loop(my_list)
print(f"The product of the list is: {result}")  # Output: The product of the list is: 120