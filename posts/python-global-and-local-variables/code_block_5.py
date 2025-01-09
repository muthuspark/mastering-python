global_var = 10

def outer_function():
  outer_var = 15
  def inner_function():
      global global_var
      global_var = 25

  inner_function()

outer_function()
print(global_var) # Output: 25