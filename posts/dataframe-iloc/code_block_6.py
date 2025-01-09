df.iloc[1, 0] = 10
print(df)

#Modify a whole column
df.iloc[:,0] = [100, 200, 300]
print(df)