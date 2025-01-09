data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 28],
        'City': ['New York', 'London', 'Paris']}

df = pd.DataFrame.from_dict(data)
print(df)

df_index = pd.DataFrame.from_dict(data, orient='index')
print(df_index)
