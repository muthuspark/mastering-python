import psycopg2

conn_params = {
    "host": "your_db_host",
    "database": "your_db_name",
    "user": "your_db_user",
    "password": "your_db_password"
}

try:
    # Connect to the database
    conn = psycopg2.connect(**conn_params)
    cursor = conn.cursor()

    #Example query (adapt to your needs)
    cursor.execute("SELECT version()")
    db_version = cursor.fetchone()
    print(f"PostgreSQL database version: {db_version}")

    #Remember to handle other database operations like in the sqlite3 example.

except psycopg2.Error as e:
    print(f"PostgreSQL error: {e}")

finally:
    if conn:
        cursor.close()
        conn.close()
