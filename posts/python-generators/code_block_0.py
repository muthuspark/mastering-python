def my_generator(n):
  for i in range(n):
    yield i

gen = my_generator(5)

for i in gen:
  print(i)  # Output: 0 1 2 3 4