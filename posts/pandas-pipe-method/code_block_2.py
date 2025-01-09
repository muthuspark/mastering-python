def square_column(df, col_name):
    df[col_name + "_squared"] = df[col_name]**2
    return df

df = df.pipe(square_column, col_name='A')
print(df)