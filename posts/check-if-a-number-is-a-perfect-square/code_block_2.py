def is_perfect_square_binary_search(n):
  """Checks if n is a perfect square using binary search.

  Args:
    n: The number to check. Must be a non-negative integer.

  Returns:
    True if n is a perfect square, False otherwise.
  """
  if n < 0:
    return False
  low, high = 0, n
  while low <= high:
    mid = (low + high) // 2
    square = mid * mid
    if square == n:
      return True
    elif square < n:
      low = mid + 1
    else:
      high = mid - 1
  return False

print(is_perfect_square_binary_search(64)) # Output: True
print(is_perfect_square_binary_search(65)) # Output: False
