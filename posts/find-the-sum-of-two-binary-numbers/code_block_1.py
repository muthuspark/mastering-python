def add_binary_bitwise(bin1, bin2):
    """Adds two binary numbers using bitwise operations."""
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)  # Pad with leading zeros for equal length
    bin2 = bin2.zfill(max_len)
    carry = 0
    result = ""
    for i in range(max_len - 1, -1, -1):
        bit1 = int(bin1[i])
        bit2 = int(bin2[i])
        sum_bits = bit1 + bit2 + carry
        result = str(sum_bits % 2) + result  #LSB
        carry = sum_bits // 2  #carry bit

    if carry:
        result = "1" + result
    return result


binary_num1 = "1011"
binary_num2 = "100"
result = add_binary_bitwise(binary_num1, binary_num2)
print(f"The sum of {binary_num1} and {binary_num2} is: {result}") # Output: 1111