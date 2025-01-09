
df['Region_Sales_Mean'] = df.groupby('Region')['Sales'].transform('mean')
print(df)
