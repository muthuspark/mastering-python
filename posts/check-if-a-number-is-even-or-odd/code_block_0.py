def is_even_odd(number):
  """Checks if a number is even or odd using the modulo operator.

  Args:
    number: An integer.

  Returns:
    "Even" if the number is even, "Odd" otherwise.
  """
  if number % 2 == 0:
    return "Even"
  else:
    return "Odd"

print(is_even_odd(10))  # Output: Even
print(is_even_odd(7))   # Output: Odd