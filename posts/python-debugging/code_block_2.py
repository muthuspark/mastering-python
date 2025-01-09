try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")