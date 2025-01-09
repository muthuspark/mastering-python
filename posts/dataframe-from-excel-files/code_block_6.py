df_typed = pd.read_excel("data.xlsx", dtype={'Age': 'Int64', 'Sales': 'float64'})
print(df_typed)
