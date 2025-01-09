import pandas as pd

data = {'Values': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)


def custom_sum(series):
  return series.sum()

def custom_range(series):
  return series.max() - series.min()


aggregated_data = df.agg({'Values': [custom_sum, custom_range]})
print(aggregated_data)
#Output:      Values
