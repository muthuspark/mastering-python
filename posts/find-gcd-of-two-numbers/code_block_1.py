def gcd_iterative(a, b):
  """
  Calculates the GCD of two numbers using an iterative approach.

  Args:
    a: The first number.
    b: The second number.

  Returns:
    The GCD of a and b.
  """
  smaller = min(a, b)
  for i in range(smaller, 0, -1):
    if a % i == 0 and b % i == 0:
      return i

num1 = 48
num2 = 18
result = gcd_iterative(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")  # Output: 6
