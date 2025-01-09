data = {'Region': ['North']*3 + ['South']*3,
        'Category': ['Electronics', 'Clothing', 'Food']*2,
        'Sales': np.random.randint(100, 1000, size=6)}
df2 = pd.DataFrame(data)
df2 = df2.set_index(['Region', 'Category'])
print(df2)