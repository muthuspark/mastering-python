pivoted_df = df.pivot_table(values='Value', index='Category', columns='Subcategory', aggfunc='sum')
print("\nPivoted DataFrame:\n", pivoted_df)