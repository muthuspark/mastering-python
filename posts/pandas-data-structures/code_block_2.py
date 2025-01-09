#Setting index
df = df.set_index('Name')
print("\nDataFrame with Name as index:\n", df)

#Resetting index
df = df.reset_index()
print("\nDataFrame with default numerical index:\n",df)
