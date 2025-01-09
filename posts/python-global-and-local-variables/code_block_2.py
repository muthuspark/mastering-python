global_var = 10

def modify_global():
  global global_var  # Declare that we are modifying the global variable
  global_var = 20

modify_global()
print(global_var)  # Output: 20