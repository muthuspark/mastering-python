def decimal_to_hex(decimal_num):
    hex_digits = "0123456789ABCDEF"
    if decimal_num == 0:
        return "0"
    hex_string = ""
    while decimal_num > 0:
        remainder = decimal_num % 16
        hex_string = hex_digits[remainder] + hex_string
        decimal_num //= 16
    return hex_string

decimal_number = 4567

hexadecimal_number = decimal_to_hex(decimal_number)

print(f"The hexadecimal representation of {decimal_number} is: {hexadecimal_number}")