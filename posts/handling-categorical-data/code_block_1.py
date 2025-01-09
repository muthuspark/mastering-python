from sklearn.preprocessing import LabelEncoder

data = {'size': ['small', 'medium', 'large', 'small']}
df = pd.DataFrame(data)

le = LabelEncoder()
df['size_encoded'] = le.fit_transform(df['size'])
print(df)