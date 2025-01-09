hex_number_without_prefix = "FF"
decimal_number = int("0x" + hex_number_without_prefix, 16)
print(f"The decimal equivalent of {hex_number_without_prefix} is: {decimal_number}")