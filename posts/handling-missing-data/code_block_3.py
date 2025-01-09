from sklearn.impute import KNNImputer
imputer = KNNImputer(n_neighbors=2) # Adjust n_neighbors as needed
df_knn_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_knn_imputed)