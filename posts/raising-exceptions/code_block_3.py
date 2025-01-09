try:
    # Some code that might raise an exception
    raise ValueError("Something went wrong")
except ValueError as e:
    print("Caught a ValueError!")
    # Perform some cleanup or logging here
    raise  # Re-raises the ValueError