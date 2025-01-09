my_input = 123  #Not a string
if isinstance(my_input, str):
    uppercase_input = my_input.upper()
else:
    print("Input must be a string")