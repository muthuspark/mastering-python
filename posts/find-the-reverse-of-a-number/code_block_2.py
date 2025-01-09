def reverse_number_recursive(n):
  """Reverses an integer using recursion (less efficient).

  Args:
    n: The integer to be reversed.

  Returns:
    The reversed integer.
  """
  if n < 0:
      return -reverse_number_recursive(-n)
  elif n < 10:
      return n
  else:
      return int(str(n % 10) + str(reverse_number_recursive(n // 10)))

#Example Usage - same output as above methods.  This is provided for educational purposes only.  Iterative method is preferred for performance
number = 12345
reversed_number = reverse_number_recursive(number)
print(f"The reverse of {number} is {reversed_number}")