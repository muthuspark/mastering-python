numbers = [1, 2, 'a', 3, 4, 5]
total = sum(num for num in numbers if isinstance(num, (int, float)))
print(f"The sum is: {total}") # Output: The sum is: 15
