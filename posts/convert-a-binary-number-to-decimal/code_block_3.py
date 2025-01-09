def binaryToDecimal(binary):
    try:
        return int(binary, 2)
    except ValueError:
        return "Invalid binary string"

print(binaryToDecimal("101101")) # Output: 45
print(binaryToDecimal("101121")) # Output: Invalid binary string
