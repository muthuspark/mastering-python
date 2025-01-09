import sqlite3

conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT
    )
''')

cursor.execute("INSERT INTO employees (name, department) VALUES (?, ?)", ('John Doe', 'Engineering'))
cursor.execute("INSERT INTO employees (name, department) VALUES (?, ?)", ('Jane Smith', 'Marketing'))

conn.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()