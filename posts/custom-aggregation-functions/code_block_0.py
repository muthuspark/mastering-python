import pandas as pd

data = {'Sales': [100, 200, 300, 400],
        'Weight': [0.1, 0.3, 0.4, 0.2]}
df = pd.DataFrame(data)

def weighted_average(series):
    weights = series['Weight']
    sales = series['Sales']
    return (sales * weights).sum() / weights.sum()


weighted_avg = df.agg(weighted_average)
print(weighted_avg) #Output: Sales    260.0