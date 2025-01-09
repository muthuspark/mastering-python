def my_function():
    try:
        return 10
    finally:
        print("Finally block executed!")
        return 20

result = my_function()
print(result) # Output: 20