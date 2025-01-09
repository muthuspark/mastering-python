try:
    # Some code that might raise an exception
    x = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    print(f"Result: {x}")
finally:
    print("This always executes.")