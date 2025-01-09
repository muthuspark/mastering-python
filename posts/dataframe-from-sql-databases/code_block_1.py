query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)

print(df)