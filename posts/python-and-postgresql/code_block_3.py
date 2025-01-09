conn = psycopg2.connect(...) # Your connection details
cur = conn.cursor()

try:
    cur.execute("UPDATE your_table SET column1 = 'new_value' WHERE id = 1;")
    cur.execute("DELETE FROM another_table WHERE id = 2;")
    conn.commit() # Commit the changes if both updates succeed
except psycopg2.Error as e:
    conn.rollback()  # Rollback the changes if an error occurs
    print(f"Transaction failed: {e}")

cur.close()
conn.close()
