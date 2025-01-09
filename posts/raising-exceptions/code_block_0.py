def validate_age(age):
  if age < 0:
    raise ValueError("Age cannot be negative")
  print(f"Age is valid: {age}")

try:
  validate_age(-5)
except ValueError as e:
  print(f"Error: {e}")

validate_age(30)