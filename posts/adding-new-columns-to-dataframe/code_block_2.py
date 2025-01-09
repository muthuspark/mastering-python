df['col7'] = df['col1'] + df['col2']
print("\nDataFrame after adding 'col7':\n", df)

#Creating 'col8' based on a conditional statement
df['col8'] = ['High' if x > 10 else 'Low' for x in df['col7']]
print("\nDataFrame after adding 'col8':\n", df)