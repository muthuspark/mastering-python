df.loc['Alice', 'Age'] = 26
print("\nDataFrame after changing Alice's age:\n", df)

#Change multiple values
df.loc[df['Age']>25,'Age']=30
print("\nDataFrame after changing ages >25:\n", df)

