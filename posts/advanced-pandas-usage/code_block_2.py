df_nan = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})

df_filled = df_nan.fillna(0)
print("\nDataFrame after filling NaN with 0:\n", df_filled)


#Filling NaN values with Forward Fill
df_ffill = df_nan.ffill()
print("\nDataFrame after Forward Fill:\n", df_ffill)


df_replaced = df_filled.replace(0, 100)
print("\nDataFrame after replacing 0 with 100:\n", df_replaced)
