def add_binary_generator(bin1, bin2):
    """Adds two binary numbers using a generator and sum()."""

    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    sum_generator = (int(bit1) + int(bit2) for bit1, bit2 in zip(bin1, bin2))
    decimal_sum = sum(sum_generator)
    return bin(decimal_sum)[2:]

#Example
binary_num1 = "1011"
binary_num2 = "100"
result = add_binary_generator(binary_num1, binary_num2)
print(f"The sum of {binary_num1} and {binary_num2} is: {result}") # Output: 1111