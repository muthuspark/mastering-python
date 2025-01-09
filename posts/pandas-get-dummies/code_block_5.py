encoded_df = pd.get_dummies(df, columns=['color', 'size'], sparse=True)
print("\nOne-hot encoded DataFrame with sparse=True:\n", encoded_df)