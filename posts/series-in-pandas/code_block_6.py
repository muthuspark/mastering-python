import pandas as pd

series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([10, 20, 30, 40, 50])

print(series1 + series2) # Element-wise addition
print(series1 * 2)      # Scalar multiplication
print(series1 > 2)      # Boolean indexing