df_filled_zero = df.fillna(0)  # Fill with 0
df_filled_mean = df['A'].fillna(df['A'].mean()) #Fill with column mean
print(df_filled_zero)
print(df_filled_mean)