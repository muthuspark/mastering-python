numbers = [x**2 for x in range(10)]
print(numbers)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

number_gen = (x**2 for x in range(10))
print(number_gen) # Output: <generator object <genexpr> at 0x...>

#Iterating through the generator
for num in number_gen:
    print(num) # Output: 0, 1, 4, 9, 16, 25, 36, 49, 64, 81