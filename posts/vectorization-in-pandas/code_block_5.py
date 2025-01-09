#Example of a less efficient use of applymap, better to vectorize whenever possible.
df['col6'] = df['col1'].applymap(lambda x: x**2)

#Much better approach
df['col7'] = df['col1']**2
