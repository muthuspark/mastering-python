def versatile_function(*args, **kwargs):
  """Demonstrates the use of both *args and **kwargs."""
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

versatile_function(1, 2, 3, name="Bob", age=25)