import sqlite3

username = input("Enter username: ")
password = input("Enter password: ")
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

username = input("Enter username: ")
password = input("Enter password: ")
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))