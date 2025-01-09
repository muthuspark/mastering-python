def add_columns(df, col1, col2, new_col_name):
    df[new_col_name] = df[col1] + df[col2]
    return df

df = df.pipe(add_columns, 'A', 'B', 'Sum_AB')
print(df)