df_copy = df.copy()

city_column = df_copy.pop('Salary')
print(df_copy)
print(city_column)