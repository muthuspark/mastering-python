def sum_of_squares_sum_generator(n):
    """Calculates the sum of squares using sum() and a generator expression."""
    if not isinstance(n, int) or n <= 0:
        return 0
    return sum(i**2 for i in range(1, n+1))

#Example Usage
n = 5
result = sum_of_squares_sum_generator(n)
print(f"The sum of squares of the first {n} natural numbers is: {result}") # Output: 55