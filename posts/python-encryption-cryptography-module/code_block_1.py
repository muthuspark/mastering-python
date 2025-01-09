from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

message = b"This is a secret message"

encrypted_message = f.encrypt(message)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = f.decrypt(encrypted_message)
print(f"Decrypted message: {decrypted_message}")