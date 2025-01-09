ordered_categories = pd.Categorical(data, categories=['banana', 'apple', 'orange'], ordered=True)
series = pd.Series(ordered_categories)
print(series.sort_values())