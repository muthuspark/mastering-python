df_with_nan = pd.DataFrame({'A': [1, 2, None, 4, 5]})
sum_with_nan = df_with_nan['A'].sum()
sum_without_nan = df_with_nan['A'].sum(skipna=False)

print(f"Sum with NaN ignored: {sum_with_nan}")
print(f"Sum with NaN included: {sum_without_nan}")