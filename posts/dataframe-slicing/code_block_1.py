df.index = ['A', 'B', 'C', 'D', 'E']

print(df.loc[['B', 'D']])

print(df.loc['B':'D'])

print(df.loc[['B', 'D'], ['col1', 'col3']])