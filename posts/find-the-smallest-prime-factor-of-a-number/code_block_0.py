def smallest_prime_factor_iterative(n):
    """Finds the smallest prime factor of a number using iteration.

    Args:
        n: The number to find the smallest prime factor of.

    Returns:
        The smallest prime factor of n, or n if n is prime.  Returns 1 if n is 1.

    Raises:
        ValueError: if n is not a positive integer.

    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")
    if n == 1:
        return 1
    for i in range(2, int(n**0.5) + 1):  # Optimization: Check only up to the square root
        if n % i == 0:
            return i
    return n  # n is prime if no factor is found

#Example usage
print(smallest_prime_factor_iterative(12))  # Output: 2
print(smallest_prime_factor_iterative(35))  # Output: 5
print(smallest_prime_factor_iterative(17))  # Output: 17
print(smallest_prime_factor_iterative(1)) # Output: 1
