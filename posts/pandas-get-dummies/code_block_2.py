encoded_df = pd.get_dummies(df, columns=['color', 'size'], prefix=['clr', 'sz'])
print("\nOne-hot encoded DataFrame with custom prefixes:\n", encoded_df)