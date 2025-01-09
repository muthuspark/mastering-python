x = [1, 2, 3]
y = [1, 2, 3]

print(x is not y)  # Output: True (different objects)

x = 10
y = 10

print(x is not y) # Output: False (for small integers, python often reuses objects for efficiency)

z = 1000
w = 1000

print(z is not w) # Output: True (for larger numbers, distinct objects might be created)