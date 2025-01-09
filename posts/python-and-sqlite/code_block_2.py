book_data = [
    ('The Hitchhiker\'s Guide to the Galaxy', 'Douglas Adams', '978-0345391803'),
    ('Pride and Prejudice', 'Jane Austen', '978-0141439518'),
    ('1984', 'George Orwell', '978-0451524935')
]

cursor.executemany("INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)", book_data)
conn.commit()

print("Book data inserted successfully!")