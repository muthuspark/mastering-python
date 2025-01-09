def fibonacci_recursive(n):
    """Recursive Fibonacci calculation. O(2^n) complexity."""
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(6)) # Output: 8
