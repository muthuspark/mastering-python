def sum_odd_numbers_comprehension(numbers):
  """Calculates the sum of odd numbers in a list using list comprehension.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of odd numbers in the list. Returns 0 if the list is empty or contains no odd numbers.
  """
  return sum([number for number in numbers if number % 2 != 0])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_sum = sum_odd_numbers_comprehension(my_list)
print(f"The sum of odd numbers is: {odd_sum}") # Output: The sum of odd numbers is: 25
