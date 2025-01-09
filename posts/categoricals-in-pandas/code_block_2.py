df = pd.DataFrame({'fruit': ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']})
df['fruit'] = pd.Categorical(df['fruit'])
print(df)