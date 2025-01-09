def add(x, y):
    return x + y

add_lambda = lambda x, y: x + y

print(add(5, 3))       # Output: 8
print(add_lambda(5, 3)) # Output: 8

#Using lambda with map
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers) # Output: [1, 4, 9, 16, 25]