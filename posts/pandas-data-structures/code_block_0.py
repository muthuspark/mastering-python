import pandas as pd

data = [10, 20, 30, 40, 50]
series_from_list = pd.Series(data)
print("Series from list:\n", series_from_list)

data = {'a': 100, 'b': 200, 'c': 300}
series_from_dict = pd.Series(data)
print("\nSeries from dictionary:\n", series_from_dict)

print("\nAccessing element with label 'b':", series_from_dict['b'])

print("\nAccessing element at index 1 (list based):", series_from_list[1])