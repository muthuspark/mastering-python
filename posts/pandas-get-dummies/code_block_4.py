encoded_df = pd.get_dummies(df, columns=['color', 'size'], drop_first=True)
print("\nOne-hot encoded DataFrame with drop_first=True:\n", encoded_df)