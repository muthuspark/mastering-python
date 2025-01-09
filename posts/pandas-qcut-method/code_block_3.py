data = {'values': np.random.randn(100), 'category': ['A']*50 + ['B']*50}
df = pd.DataFrame(data)

df['quantiles'] = pd.qcut(df['values'], 4)
print(df.head())