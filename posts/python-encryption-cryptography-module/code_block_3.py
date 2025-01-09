from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(b"This is some data")
hashed_data = digest.finalize()
print(f"Hashed data: {hashed_data}")
