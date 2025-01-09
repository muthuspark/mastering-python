print("\nRows where Age > 25:\n", df.loc[df['Age'] > 25])

print("\nRows where City is 'Paris' or 'Tokyo':\n", df.loc[(df['City'] == 'Paris') | (df['City'] == 'Tokyo')])