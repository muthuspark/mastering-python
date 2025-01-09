def sum_even_numbers_comprehension(numbers):
  """Calculates the sum of even numbers in a list using list comprehension.

  Args:
    numbers: A list of integers.

  Returns:
    The sum of even numbers in the list. Returns 0 if the list is empty or contains no even numbers.
  """
  return sum([number for number in numbers if number % 2 == 0])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum_even_numbers_comprehension(my_list)
print(f"The sum of even numbers is: {even_sum}") # Output: The sum of even numbers is: 30