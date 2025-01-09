df.drop_duplicates(subset=['col1'], keep='first', inplace=True)
print(df)