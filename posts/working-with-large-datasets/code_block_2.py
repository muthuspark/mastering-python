import vaex

df = vaex.open("large_dataset.csv")

mean_value = df["column_name"].mean()
print(mean_value)
