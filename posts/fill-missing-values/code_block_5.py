from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='mean') #Other strategies: 'median', 'most_frequent'
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_imputed)