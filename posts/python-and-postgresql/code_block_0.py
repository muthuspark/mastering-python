import psycopg2

try:
    conn = psycopg2.connect(
        host="your_db_host",  # e.g., "localhost"
        database="your_db_name",  # e.g., "mydatabase"
        user="your_db_user",  # e.g., "yourusername"
        password="your_db_password"  # e.g., "yourpassword"
    )
    print("Connected to PostgreSQL successfully!")
except psycopg2.Error as e:
    print(f"Error connecting to PostgreSQL: {e}")