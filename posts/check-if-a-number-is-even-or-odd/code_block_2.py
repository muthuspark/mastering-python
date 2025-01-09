def is_even_odd_robust(number):
  """Checks if a number is even or odd, handling non-integer inputs.

  Args:
    number: A number.

  Returns:
    "Even" if the number is an even integer, "Odd" if it's an odd integer,
    and an error message otherwise.
  """
  try:
    number = int(number)
    if number % 2 == 0:
      return "Even"
    else:
      return "Odd"
  except ValueError:
    return "Invalid input: Please provide an integer."

print(is_even_odd_robust(10))      # Output: Even
print(is_even_odd_robust(7.5))     # Output: Invalid input: Please provide an integer.
print(is_even_odd_robust("hello")) # Output: Invalid input: Please provide an integer.
