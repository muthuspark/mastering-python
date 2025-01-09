memo = {}  # Dictionary to store calculated Fibonacci numbers

def fibonacci_dynamic(n):
  """
  Calculates the nth Fibonacci number using dynamic programming (memoization).

  Args:
    n: The index of the desired Fibonacci number (starting from 0).

  Returns:
    The nth Fibonacci number.
  """
  if n in memo:
    return memo[n]
  if n <= 1:
    result = n
  else:
    result = fibonacci_dynamic(n-1) + fibonacci_dynamic(n-2)
  memo[n] = result
  return result

print(fibonacci_dynamic(6))  # Output: 8