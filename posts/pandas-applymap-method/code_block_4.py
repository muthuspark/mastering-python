def my_func(x):
    try:
        return 1/x
    except ZeroDivisionError:
        return np.nan  # Handle division by zero

data = {'A': [1, 0, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

result_df = df.applymap(my_func)
print(result_df)