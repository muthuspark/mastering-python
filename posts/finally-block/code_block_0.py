try:
    # Code that might raise an exception
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    print("Error: Division by zero!")
finally:
    print("This always executes!")