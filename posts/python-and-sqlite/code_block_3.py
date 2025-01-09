cursor.execute("SELECT * FROM books")
books = cursor.fetchall()

for book in books:
    print(book)