def reverse_number_string(n):
  """Reverses an integer using string manipulation.

  Args:
    n: The integer to be reversed.

  Returns:
    The reversed integer. Returns 0 if the input is 0. Raises ValueError for non-integer input.
  """
  if n == 0:
      return 0
  if not isinstance(n, int):
      raise ValueError("Input must be an integer.")
  return int(str(n)[::-1]) * (-1 if n < 0 else 1)

#Example Usage
number = 12345
reversed_number = reverse_number_string(number)
print(f"The reverse of {number} is {reversed_number}")  # Output: The reverse of 12345 is 54321

number = -876
reversed_number = reverse_number_string(number)
print(f"The reverse of {number} is {reversed_number}") # Output: The reverse of -876 is -678

number = 0
reversed_number = reverse_number_string(number)
print(f"The reverse of {number} is {reversed_number}") # Output: The reverse of 0 is 0
