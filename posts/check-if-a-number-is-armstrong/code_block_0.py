def is_armstrong_number(num):
  """Checks if a number is an Armstrong number (basic approach)."""
  num_str = str(num)
  num_digits = len(num_str)
  sum_of_powers = 0
  for digit in num_str:
    sum_of_powers += int(digit) ** num_digits
  return sum_of_powers == num

number = 153
if is_armstrong_number(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")

number = 123
if is_armstrong_number(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")
