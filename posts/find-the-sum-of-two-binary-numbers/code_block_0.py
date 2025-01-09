def add_binary_decimal(bin1, bin2):
  """Adds two binary numbers by converting them to decimal first."""
  decimal1 = int(bin1, 2)  # Convert binary string to decimal
  decimal2 = int(bin2, 2)
  decimal_sum = decimal1 + decimal2
  binary_sum = bin(decimal_sum)[2:] # Convert decimal sum back to binary, [2:] removes "0b" prefix
  return binary_sum

#Example
binary_num1 = "1011"
binary_num2 = "100"
result = add_binary_decimal(binary_num1, binary_num2)
print(f"The sum of {binary_num1} and {binary_num2} is: {result}") #Output: 1111
