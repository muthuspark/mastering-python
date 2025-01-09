def gcd_euclidean(a, b):
  """
  Calculates the GCD of two numbers using the Euclidean algorithm.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The GCD of a and b.
  """
  while(b):
    a, b = b, a % b
  return a

num1 = 48
num2 = 18
result = gcd_euclidean(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")  # Output: 6