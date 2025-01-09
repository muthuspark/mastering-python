float_num = 3.14159
int_num = int(float_num)  # Truncates the decimal part
print(int_num)  # Output: 3

string_num = "10"
int_num2 = int(string_num)
print(int_num2) # Output: 10

#Error Handling
try:
  invalid_int = int("abc")
except ValueError:
  print("Error: Cannot convert 'abc' to an integer")
