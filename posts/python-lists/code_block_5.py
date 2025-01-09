numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]
print(squares)  # Output: [1, 4, 9, 16, 25]

even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers) # Output: [2, 4]
