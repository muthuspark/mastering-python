data = {'A': [1, 2, np.nan, 4, 5], 
        'B': [6, np.nan, 8, 9, 10], 
        'C': [11, 12, 13, 14, 15]}
df = pd.DataFrame(data)
print(df.count(axis=1))