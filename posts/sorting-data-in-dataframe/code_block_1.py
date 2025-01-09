sorted_df_city_age = df.sort_values(['City', 'Age'])
print("\nSorted by City then Age:\n", sorted_df_city_age)

sorted_df_city_age_mixed = df.sort_values(['City', 'Age'], ascending=[True, False])
print("\nSorted by City (asc) then Age (desc):\n", sorted_df_city_age_mixed)