def count_set_bits_method1(n):
  """Counts set bits using bin() and count().

  Args:
    n: The input integer.

  Returns:
    The number of set bits in n.
  """
  binary = bin(n)[2:]  # [2:] removes the "0b" prefix
  return binary.count('1')

number = 10  # Binary: 1010
set_bits = count_set_bits_method1(number)
print(f"The number of set bits in {number} is: {set_bits}") # Output: 2