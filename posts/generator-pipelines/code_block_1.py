def even_numbers(numbers):
  for num in numbers:
    if num % 2 == 0:
      yield num

def square_numbers(numbers):
  for num in numbers:
    yield num * num

numbers = range(10)
even_squared = (num for num in square_numbers(even_numbers(numbers)))

for num in even_squared:
  print(num)  # Output: 0 4 16 36 64