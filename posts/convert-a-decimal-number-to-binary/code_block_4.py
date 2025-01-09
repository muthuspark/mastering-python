def decimal_to_binary(decimal_num):
  """Converts a decimal number to its binary equivalent."""
  if decimal_num == 0:
    return "0"

  binary_string = ""
  while decimal_num > 0:
    remainder = decimal_num % 2
    binary_string = str(remainder) + binary_string  # Prepend remainder
    decimal_num //= 2

  return binary_string

decimal_number = 42
binary_representation = decimal_to_binary(decimal_number)
print(f"The binary representation of {decimal_number} is: {binary_representation}")
