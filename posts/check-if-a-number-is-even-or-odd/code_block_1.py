def is_even_odd_bitwise(number):
  """Checks if a number is even or odd using the bitwise AND operator.

  Args:
    number: An integer.

  Returns:
    "Even" if the number is even, "Odd" otherwise.
  """
  if number & 1 == 0:
    return "Even"
  else:
    return "Odd"

print(is_even_odd_bitwise(10))  # Output: Even
print(is_even_odd_bitwise(7))   # Output: Odd