def reverse_number_iterative(n):
  """Reverses an integer using an iterative approach.

  Args:
    n: The integer to be reversed.

  Returns:
    The reversed integer.  Returns 0 if the input is 0.
  """
  reversed_num = 0
  if n == 0:
      return 0
  if n < 0:
      sign = -1
      n = -n
  else:
      sign = 1
  while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10
  return reversed_num * sign

number = 12345
reversed_number = reverse_number_iterative(number)
print(f"The reverse of {number} is {reversed_number}")  # Output: The reverse of 12345 is 54321

number = -876
reversed_number = reverse_number_iterative(number)
print(f"The reverse of {number} is {reversed_number}") # Output: The reverse of -876 is -678

number = 0
reversed_number = reverse_number_iterative(number)
print(f"The reverse of {number} is {reversed_number}") # Output: The reverse of 0 is 0