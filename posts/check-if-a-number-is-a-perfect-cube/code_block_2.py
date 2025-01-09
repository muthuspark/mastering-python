def is_perfect_cube_method3(n):
    """Checks if a number is a perfect cube using int() for improved accuracy."""
    if n < 0:
        return False
    cbrt = int(round(n**(1/3)))
    return cbrt**3 == n

print(is_perfect_cube_method3(8))   # Output: True
print(is_perfect_cube_method3(27))  # Output: True
print(is_perfect_cube_method3(10))  # Output: False
print(is_perfect_cube_method3(-8)) # Output: False