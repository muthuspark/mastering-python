def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age

try:
    validated_age = validate_age(-5)
except ValueError as e:
    print(e)