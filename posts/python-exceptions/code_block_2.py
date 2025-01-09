def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age is unrealistically high")
    return True

try:
  check_age(-5)
except ValueError as e:
  print(e)