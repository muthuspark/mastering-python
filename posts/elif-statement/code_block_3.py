data = 10

if isinstance(data, int):
    print("It's an integer.")
elif isinstance(data, str):
    print("It's a string.")
elif isinstance(data, float):
    print("It's a float.")
else:
    print("It's another data type.") # Output: It's an integer.