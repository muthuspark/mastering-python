df_copy = df.copy()

df_copy = df_copy.drop('Age', axis=1)
print(df_copy)

#Remove multiple columns
df_copy = df.copy()
df_copy = df_copy.drop(['Age', 'City'], axis=1)
print(df_copy)

#Inplace Modification
df_copy = df.copy()
df_copy.drop('Name', axis=1, inplace=True)
print(df_copy)