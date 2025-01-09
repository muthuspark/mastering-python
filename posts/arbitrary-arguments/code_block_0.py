def my_sum(*args):
  """Calculates the sum of all input numbers."""
  total = 0
  for number in args:
    total += number
  return total

print(my_sum(1, 2, 3))  # Output: 6
print(my_sum(10, 20, 30, 40, 50))  # Output: 150
print(my_sum()) # Output: 0
