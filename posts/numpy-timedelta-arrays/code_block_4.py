timedeltas_with_nan = np.array([1, 2, np.nan], dtype='timedelta64[D]')
print(timedeltas_with_nan)

result_nan = timedeltas_with_nan + np.array([4, 5, 6], dtype='timedelta64[D]')
print(result_nan)