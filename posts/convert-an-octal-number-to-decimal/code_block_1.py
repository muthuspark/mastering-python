def octalToDecimal(octal):
  decimal = 0
  power = 0
  for digit in reversed(octal):
    decimal += int(digit) * (8 ** power)
    power += 1
  return decimal

octal_number = "753"
decimal_equivalent = octalToDecimal(octal_number)
print(f"The decimal equivalent of {octal_number} is: {decimal_equivalent}")
