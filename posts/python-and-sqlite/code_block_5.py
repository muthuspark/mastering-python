cursor.execute("UPDATE books SET title = ? WHERE id = ?", ('The Definitive Hitchhiker\'s Guide', 1))
conn.commit()

cursor.execute("DELETE FROM books WHERE id = ?", (3,))
conn.commit()