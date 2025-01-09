data = {'satisfaction': ['very satisfied', 'satisfied', 'neutral', 'dissatisfied', 'very dissatisfied']}
df = pd.DataFrame(data)
mapping = {'very satisfied': 4, 'satisfied': 3, 'neutral': 2, 'dissatisfied': 1, 'very dissatisfied': 0}
df['satisfaction_encoded'] = df['satisfaction'].map(mapping)
print(df)