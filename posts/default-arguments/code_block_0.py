def greet(name, greeting="Hello"):
  """Greets a person with a customizable greeting."""
  print(f"{greeting}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob", "Good morning")  # Output: Good morning, Bob!