df = (df
      .pipe(square_column, col_name='B')
      .pipe(add_columns, 'A', 'B_squared', 'A_plus_B_squared')
     )
print(df)