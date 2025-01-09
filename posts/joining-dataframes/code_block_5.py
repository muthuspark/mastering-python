df3 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'ProductID': [10, 20, 30],
    'Quantity': [2,1,3]
})

df4 = pd.DataFrame({
    'CustomerID': [1, 1, 2],
    'ProductID': [10, 20, 20],
    'Price': [100,200, 150]
})

multi_key_join = pd.merge(df3, df4, on=['CustomerID', 'ProductID'], how='left')
print("\nMulti-key Join:\n", multi_key_join)