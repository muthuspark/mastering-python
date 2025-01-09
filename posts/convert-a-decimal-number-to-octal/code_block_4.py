def decimal_to_octal(decimal_num):
  """Converts a decimal number to its octal equivalent."""
  if decimal_num == 0:
    return "0"

  octal_num = ""
  while decimal_num > 0:
    remainder = decimal_num % 8
    octal_num = str(remainder) + octal_num  # Prepend the remainder
    decimal_num //= 8

  return octal_num

decimal_number = 1234
octal_representation = decimal_to_octal(decimal_number)
print(f"The octal representation of {decimal_number} is: {octal_representation}")