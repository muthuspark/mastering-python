global_var = 10

def my_function():
  local_var = 5
  print(global_var)  # Accessing global variable
  # print(global_var + local_var)

my_function()
#print(local_var) #This will cause an error because local_var is not accessible outside the function.