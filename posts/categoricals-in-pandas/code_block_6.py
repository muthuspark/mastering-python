df['fruit'] = df['fruit'].cat.remove_categories(['grape'])
print(df)