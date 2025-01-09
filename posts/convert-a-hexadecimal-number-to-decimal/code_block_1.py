def hex_to_decimal(hex_str):
  """Converts a hexadecimal string to its decimal equivalent."""
  decimal_value = 0
  power = 0
  for digit in reversed(hex_str):
    if '0' <= digit <= '9':
      value = ord(digit) - ord('0')
    elif 'A' <= digit <= 'F':
      value = ord(digit) - ord('A') + 10
    elif 'a' <= digit <= 'f':
      value = ord(digit) - ord('a') + 10
    else:
      raise ValueError("Invalid hexadecimal character")
    decimal_value += value * (16 ** power)
    power += 1
  return decimal_value

hex_number = "1A"
decimal_equivalent = hex_to_decimal(hex_number)
print(f"The decimal equivalent of {hex_number} is: {decimal_equivalent}")
