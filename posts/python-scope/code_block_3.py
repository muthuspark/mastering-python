global_var = 40

def modify_global():
  global global_var  # Declare global_var as a global variable
  global_var = 50

modify_global()
print(global_var)  # Output: 50