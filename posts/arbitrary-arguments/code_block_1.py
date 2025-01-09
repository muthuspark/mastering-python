def print_details(**kwargs):
  """Prints the key-value pairs from keyword arguments."""
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_details(name="Alice", age=30, city="New York")

print_details(country="USA", profession="Engineer")