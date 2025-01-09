float_num = 3.14
int_num = int(float_num)  # Truncates the decimal part
print(int_num)  # Output: 3
print(type(int_num)) # Output: <class 'int'>

string_num = "10"
int_num2 = int(string_num)
print(int_num2) # Output: 10
print(type(int_num2)) # Output: <class 'int'>

#Error Handling
try:
    int_num3 = int("10a")
except ValueError as e:
    print(f"Error converting string to integer: {e}") # Output: Error converting string to integer: invalid literal for int() with base 10: '10a'
