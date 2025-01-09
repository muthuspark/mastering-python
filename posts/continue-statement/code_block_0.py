numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 != 0:  # Check if the number is odd
        continue  # Skip to the next iteration if odd
    print(f"Even number: {number}")