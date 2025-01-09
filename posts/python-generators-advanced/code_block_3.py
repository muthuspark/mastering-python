def closing_generator():
    try:
        yield 1
        yield 2
        yield 3
    except GeneratorExit:
        print("Generator closed gracefully")

gen = closing_generator()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
gen.close()