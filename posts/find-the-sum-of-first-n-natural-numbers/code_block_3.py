def sum_n_sum_range(n):
    """
    Calculates the sum using the built-in sum() and range() functions.
    Args:
      n: The number of natural numbers to sum.
    Returns:
      The sum of the first n natural numbers. Returns 0 if n is 0 or negative.
    """
    if n <= 0:
        return 0
    return sum(range(1, n + 1))

print(sum_n_sum_range(5))  # Output: 15
print(sum_n_sum_range(100)) # Output: 5050