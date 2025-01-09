data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Grade': ['10', '10', '11'],
        'Math': [85, 92, 78],
        'Science': [90, 88, 95]}
df = pd.DataFrame(data)
melted_df = df.melt(id_vars=['Name', 'Grade'], var_name='Subject', value_name='Score')
print(melted_df)