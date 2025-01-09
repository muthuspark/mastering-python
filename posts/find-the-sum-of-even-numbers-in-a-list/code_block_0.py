def sum_even_numbers_loop(numbers):
  """Calculates the sum of even numbers in a list using a for loop.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of even numbers in the list.  Returns 0 if the list is empty or contains no even numbers.
  """
  total = 0
  for number in numbers:
    if number % 2 == 0:
      total += number
  return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum_even_numbers_loop(my_list)
print(f"The sum of even numbers is: {even_sum}") # Output: The sum of even numbers is: 30