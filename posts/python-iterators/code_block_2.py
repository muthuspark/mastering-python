def my_generator(n):
    for i in range(n):
        yield i * 2

for item in my_generator(5):
    print(item) # Output: 0 2 4 6 8