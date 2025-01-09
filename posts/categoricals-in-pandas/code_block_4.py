df['fruit'] = df['fruit'].cat.rename_categories({'apple': 'Apple', 'banana': 'Banana'})
print(df)
