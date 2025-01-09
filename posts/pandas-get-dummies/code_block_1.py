data = {'color': ['red', 'green', 'blue', 'red', 'green'],
        'size': ['small', 'medium', 'large', 'small', 'medium']}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

encoded_df = pd.get_dummies(df, columns=['color', 'size'])
print("\nOne-hot encoded DataFrame:\n", encoded_df)