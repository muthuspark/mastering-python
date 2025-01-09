def square(x):
    return x**2

df['col9'] = df['col1'].apply(square)
print("\nDataFrame after adding 'col9':\n", df)