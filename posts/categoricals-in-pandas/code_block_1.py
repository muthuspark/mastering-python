ordered_categories = pd.Categorical(data, categories=['banana', 'apple', 'orange'], ordered=True)
print(ordered_categories)
#ordered=True makes the category ordered, enabling comparison operations.