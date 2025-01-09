def outer_function():
  y = 20  # Enclosing function variable

  def inner_function():
    print(y)  # Accessing y from the enclosing function

  inner_function()

outer_function()  # Output: 20