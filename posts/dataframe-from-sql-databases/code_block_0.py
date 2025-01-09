import sqlite3
import pandas as pd

conn = sqlite3.connect('your_database.db')

cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        salary REAL
    )
''')
conn.commit()

cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", ("Alice", "Sales", 60000))
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", ("Bob", "Engineering", 75000))
cursor.execute("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", ("Charlie", "Sales", 65000))
conn.commit()