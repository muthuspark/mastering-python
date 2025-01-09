def my_generator():
    value = 0
    while True:
        received = yield value
        if received is not None:
            value += received
        else:
            value += 1


gen = my_generator()
print(next(gen))  # Output: 0 (Initial value)
print(gen.send(5)) # Output: 5 (0 + 5)
print(gen.send(3)) # Output: 8 (5 + 3)