x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  # Output: False (different objects in memory)
z = x
print(x is z) # Output: True (x and z refer to the same object)