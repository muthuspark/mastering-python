df_dropped_rows = df.dropna()
print(df_dropped_rows)

df_dropped_cols = df.dropna(axis=1)
print(df_dropped_cols)