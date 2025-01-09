decimal_number = 255

octal_number = oct(decimal_number)[2:] # [2:] slices the string from the third character onwards

print(f"The octal equivalent of {decimal_number} is: {octal_number}")