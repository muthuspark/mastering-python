x = [1, 2, 3]
y = x  # y now points to the same list object as x

print(x is y)  # Output: True
print(x == y)  # Output: True (value equality)


a = [1, 2, 3]
b = [1, 2, 3]  # a and b are distinct list objects, even if they have the same values.

print(a is b)  # Output: False (different memory locations)
print(a == b)  # Output: True (value equality)