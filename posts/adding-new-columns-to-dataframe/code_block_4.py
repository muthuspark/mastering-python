#Adding multiple columns at once using assign
new_df = df.assign(col10 = df['col1'] * 2, col11 = df['col2'] / 2)
print("\nNew DataFrame after using assign:\n",new_df)
print("\nOriginal DataFrame remains unchanged:\n", df)