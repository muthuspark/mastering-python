print("\nRows from 'Bob' to 'David':\n", df.loc['Bob':'David'])

print("\nRows 0-2 (inclusive) using labels:\n", df.loc[:2])

#Select specific rows and columns
print("\nRows from 'Bob' to 'Charlie', 'Age' and 'City' columns:\n", df.loc['Bob':'Charlie',['Age','City']])

