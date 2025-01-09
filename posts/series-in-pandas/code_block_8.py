import pandas as pd

series1 = pd.Series({'a': 1, 'b': 2, 'c': 3})
series2 = pd.Series({'b': 4, 'c': 5, 'd': 6})

print(series1 + series2)  # Notice how NaN appears where indices don't match