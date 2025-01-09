binary_number = "101101"
decimal_number = 0
power = 0

for digit in reversed(binary_number):
    if digit == '1':
        decimal_number += 2**power
    power += 1

print(f"The decimal equivalent of {binary_number} is: {decimal_number}")