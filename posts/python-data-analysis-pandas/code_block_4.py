print(df['Name'])          # Select the 'Name' column
print(df[df['Age'] > 28]) # Filter rows where Age > 28
df['Country'] = ['USA', 'UK', 'France'] # Add a new column
print(df)