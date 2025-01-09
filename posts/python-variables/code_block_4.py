global_var = 100

def my_function():
  local_var = 50
  print(global_var) # Accessing global variable
  print(local_var) # Accessing local variable

my_function()
print(global_var) # Accessing global variable
#print(local_var) # This would cause an error because local_var is not in global scope