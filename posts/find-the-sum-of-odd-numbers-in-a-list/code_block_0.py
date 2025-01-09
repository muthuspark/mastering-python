def sum_odd_numbers_loop(numbers):
  """Calculates the sum of odd numbers in a list using a for loop.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of odd numbers in the list.  Returns 0 if the list is empty or contains no odd numbers.
  """
  total = 0
  for number in numbers:
    if number % 2 != 0:
      total += number
  return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_sum = sum_odd_numbers_loop(my_list)
print(f"The sum of odd numbers is: {odd_sum}") # Output: The sum of odd numbers is: 25