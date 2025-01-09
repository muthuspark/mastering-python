decimal_num = 10
binary_num = bin(decimal_num)  # Output: 0b1010 (0b indicates binary)
print(binary_num)

#Binary to Decimal
binary_string = "0b1010"
decimal_from_binary = int(binary_string, 2) # 2 specifies base 2 (binary)
print(decimal_from_binary)

#Decimal to Hexadecimal
hexadecimal_num = hex(decimal_num) #Output: 0xa
print(hexadecimal_num)

#Hexadecimal to Decimal
hex_string = "0xa"
decimal_from_hex = int(hex_string, 16) #16 specifies base 16 (hexadecimal)
print(decimal_from_hex)


#Decimal to Octal
octal_num = oct(decimal_num) #Output: 0o12
print(octal_num)

#Octal to Decimal
oct_string = "0o12"
decimal_from_oct = int(oct_string, 8) #8 specifies base 8 (octal)
print(decimal_from_oct)
