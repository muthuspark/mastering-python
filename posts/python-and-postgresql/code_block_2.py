import psycopg2
from datetime import datetime

conn = psycopg2.connect(...) # Your connection details

cur = conn.cursor()

timestamp = datetime.now()
cur.execute("INSERT INTO your_table (date_column) VALUES (%s);", (timestamp,))
conn.commit()

cur.close()
conn.close()