def my_func():
  global global_var #declare global_var can be modified in the function.
  global_var = 50
  print(f"Inside function : global_var = {global_var}")

my_func()
print(f"Outside function : global_var = {global_var}")
#Output:
#Inside function : global_var = 50
#Outside function : global_var = 50