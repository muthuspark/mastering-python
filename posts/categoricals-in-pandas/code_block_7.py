df['fruit'] = df['fruit'].cat.set_categories(['Banana', 'Apple', 'Orange'])
print(df)