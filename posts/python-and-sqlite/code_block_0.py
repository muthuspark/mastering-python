import sqlite3

conn = sqlite3.connect('mydatabase.db') # Creates the database file if it doesn't exist
cursor = conn.cursor()  # Creates a cursor object to execute SQL commands

print("Database connected successfully!")