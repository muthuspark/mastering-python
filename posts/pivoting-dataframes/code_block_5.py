df_unique = df.drop_duplicates() #Ensure uniqueness if not already unique
pivoted_df_simple = df_unique.pivot(index='Category', columns='Subcategory', values='Value')
print("\nPivoted DataFrame using pivot():\n", pivoted_df_simple)
