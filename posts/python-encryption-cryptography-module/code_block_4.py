from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password = b"mysecretpassword"  # NEVER store passwords directly! Use a secure password manager.
salt = b"somesalt"  # Randomly generated salt is crucial for security.
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000
)
key = kdf.derive(password)
print(f"Derived key: {key}")