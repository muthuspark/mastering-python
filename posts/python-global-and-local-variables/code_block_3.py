global_var = 10

def modify_global():
  global_var = 20 #This creates a new local variable

modify_global()
print(global_var)  # Output: 10 (the global variable remains unchanged)