def factorial(n):
    """Calculates the factorial of a non-negative integer.

    Args:
        n: A non-negative integer.

    Returns:
        The factorial of n.  Returns 1 if n is 0.
        Raises ValueError if n is negative.

    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.") #Error handling explained
    elif n == 0:
        return 1 #Base case handled
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i #iterative calculation of factorial.
        return result

print(factorial(5)) # Output: 120
print(factorial(0)) # Output: 1

try:
    print(factorial(-1)) #This will raise a ValueError
except ValueError as e:
    print("Error:", e) #catching and handling the exception
