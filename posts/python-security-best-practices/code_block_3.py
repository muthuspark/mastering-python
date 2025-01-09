import bcrypt

password = input("Enter password: ")
hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
print(hashed_password)

stored_hashed_password = #... retrieved from database
if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password):
    print("Password matches!")