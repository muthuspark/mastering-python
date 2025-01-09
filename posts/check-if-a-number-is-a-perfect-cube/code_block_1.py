def is_perfect_cube_method2(n):
  """
  Checks if a number is a perfect cube using binary search.

  Args:
    n: The number to check.

  Returns:
    True if n is a perfect cube, False otherwise.
  """
  if n < 0:
    return False
  low, high = 0, n
  while low <= high:
    mid = (low + high) // 2
    cube = mid**3
    if cube == n:
      return True
    elif cube < n:
      low = mid + 1
    else:
      high = mid - 1
  return False

print(is_perfect_cube_method2(8))   # Output: True
print(is_perfect_cube_method2(27))  # Output: True
print(is_perfect_cube_method2(10))  # Output: False
print(is_perfect_cube_method2(-8)) # Output: False