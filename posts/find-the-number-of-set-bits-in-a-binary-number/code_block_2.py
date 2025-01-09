def count_set_bits_method3(n):
  """Counts set bits using the bit_count() method (Python 3.10+).

  Args:
    n: The input integer.

  Returns:
    The number of set bits in n.
  """
  return n.bit_count()

number = 10  # Binary: 1010
set_bits = count_set_bits_method3(number)
print(f"The number of set bits in {number} is: {set_bits}") # Output: 2