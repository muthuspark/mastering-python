decimal = 255
binary = bin(decimal)  # Convert to binary
octal = oct(decimal)   # Convert to octal
hexadecimal = hex(decimal) #Convert to hexadecimal

print(f"Binary: {binary}")       # Output: Binary: 0b11111111
print(f"Octal: {octal}")        # Output: Octal: 0o377
print(f"Hexadecimal: {hexadecimal}") # Output: Hexadecimal: 0xff

#Converting back to decimal
decimal_from_binary = int(binary, 2)
decimal_from_octal = int(octal, 8)
decimal_from_hex = int(hexadecimal, 16)
print(decimal_from_binary) #Output 255
print(decimal_from_octal) #Output 255
print(decimal_from_hex) #Output 255
