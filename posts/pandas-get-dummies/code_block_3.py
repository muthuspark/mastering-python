encoded_df = pd.get_dummies(df, columns=['color', 'size'], dtype=bool)
print("\nOne-hot encoded DataFrame with boolean dtype:\n", encoded_df)