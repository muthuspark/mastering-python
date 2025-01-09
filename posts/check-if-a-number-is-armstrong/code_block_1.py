def is_armstrong_number_efficient(num):
    """Checks if a number is an Armstrong number (efficient approach)."""
    original_num = num
    num_digits = len(str(num)) #We still need to determine number of digits
    sum_of_powers = 0
    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** num_digits
        num //= 10
    return sum_of_powers == original_num

number = 370
if is_armstrong_number_efficient(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")

number = 9474
if is_armstrong_number_efficient(number):
  print(f"{number} is an Armstrong number.")
else:
  print(f"{number} is not an Armstrong number.")
