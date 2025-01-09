import math

def lcm_math(a, b):
    """Calculates the LCM using the math module's gcd function."""
    return (a * b) // math.gcd(a, b)

#Example Usage
num1 = 24
num2 = 36
print(f"The LCM of {num1} and {num2} using math module is: {lcm_math(num1, num2)}")