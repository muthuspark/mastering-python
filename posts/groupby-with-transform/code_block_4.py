from scipy.stats import zscore

def standardize(x):
  return zscore(x)

standardized_sales = df.groupby('Region')['Sales'].transform(standardize)
df['Standardized_Sales'] = standardized_sales
print(df)