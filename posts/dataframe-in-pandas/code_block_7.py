df['Salary'] = [50000, 60000, float('NaN')]
print(df)
print(df.dropna()) # Removes rows with missing values
