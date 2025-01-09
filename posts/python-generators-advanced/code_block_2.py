def exception_generator():
    try:
        yield 1
        yield 2
        yield 3
    except ValueError:
        yield "Caught ValueError"


gen = exception_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
try:
  print(gen.throw(ValueError("Something went wrong"))) # Output: Caught ValueError
except StopIteration:
    print("Generator finished")

print(next(gen)) #raises StopIteration