cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT,
        isbn TEXT
    )
''')
conn.commit() # Save changes to the database

print("Table 'books' created successfully!")