def sum_even_numbers_filter(numbers):
  """Calculates the sum of even numbers in a list using filter and sum.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of even numbers in the list. Returns 0 if the list is empty or contains no even numbers.
  """
  return sum(filter(lambda x: x % 2 == 0, numbers))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum_even_numbers_filter(my_list)
print(f"The sum of even numbers is: {even_sum}") # Output: The sum of even numbers is: 30