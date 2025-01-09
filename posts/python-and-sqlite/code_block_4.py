cursor.execute("SELECT * FROM books WHERE author = ?", ('Jane Austen',))
austen_books = cursor.fetchall()
print(austen_books)