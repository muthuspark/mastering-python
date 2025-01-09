df_dropped_cols = df.dropna(axis=1, how='any')
print(df_dropped_cols)

df_dropped_cols_all = df.dropna(axis=1, how='all')
print(df_dropped_cols_all)
