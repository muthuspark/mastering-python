import bcrypt

def hash_password(password):
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')

def check_password(password, hashed_password):
  """Check if a password matches a hashed password."""
  return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

hashed = hash_password("mysecretpassword")
print(f"Hashed password: {hashed}")
print(f"Password matches: {check_password('mysecretpassword', hashed)}")
print(f"Password matches (incorrect): {check_password('wrongpassword', hashed)}")