data = pd.read_csv("data.tsv", sep='\t', header=None, names=['ColumnA', 'ColumnB', 'ColumnC'])
print(data.head())