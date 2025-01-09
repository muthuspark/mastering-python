try:
    octal_number = "128" #This contains an invalid octal digit
    decimal_equivalent = int(octal_number, 8)
    print(f"The decimal equivalent of {octal_number} is: {decimal_equivalent}")
except ValueError:
    print(f"Invalid octal number: {octal_number}")