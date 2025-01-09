def count_set_bits_method2(n):
  """Counts set bits using Brian Kernighan's algorithm.

  Args:
    n: The input integer.

  Returns:
    The number of set bits in n.
  """
  count = 0
  while n > 0:
    n &= (n - 1)  # Clears the least significant set bit
    count += 1
  return count

number = 10  # Binary: 1010
set_bits = count_set_bits_method2(number)
print(f"The number of set bits in {number} is: {set_bits}") # Output: 2