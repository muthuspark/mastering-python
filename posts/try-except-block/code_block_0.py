try:
    # Code that might raise an exception
    result = 10 / 0  # This will cause a ZeroDivisionError
except ZeroDivisionError:
    # Code to handle the specific exception
    print("Error: Division by zero!")