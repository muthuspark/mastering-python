#Example with missing data (add a NaN value)
df.loc[1, 'Country'] = float('NaN')
print(df.isnull().sum()) #check for null values
print(df.dropna())       # Remove rows with missing data