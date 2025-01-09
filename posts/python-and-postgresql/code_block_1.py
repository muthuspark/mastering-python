cur = conn.cursor()

cur.execute("SELECT * FROM your_table;") # Replace 'your_table' with your table name
rows = cur.fetchall()

for row in rows:
    print(row)

cur.execute("INSERT INTO your_table (column1, column2) VALUES (%s, %s);", ('value1', 'value2')) # Use parameterized queries to prevent SQL injection
conn.commit() # Commit changes to the database

cur.close()
conn.close()