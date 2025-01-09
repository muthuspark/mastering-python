def gcd(a, b):
  """
  Calculates the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.
  """
  while(b):
    a, b = b, a % b
  return a

def lcm(a, b):
  """
  Calculates the Least Common Multiple (LCM) of two numbers using the GCD.
  """
  return (a * b) // gcd(a, b)

#Example usage
num1 = 12
num2 = 18
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")