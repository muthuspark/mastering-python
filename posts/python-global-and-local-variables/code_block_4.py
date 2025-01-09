def outer_function():
  outer_var = 15

  def inner_function():
    print(outer_var) # inner_function can access outer_var

  inner_function()

outer_function() # Output: 15
#print(outer_var) # This will cause an error because outer_var is not accessible here.