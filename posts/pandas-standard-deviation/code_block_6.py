data = {'values': [10, 12, 15, 14, 18, None, 11, 13]}
series_with_nan = pd.Series(data['values'])
std_dev_with_nan = series_with_nan.std() #NaNs are skipped by default

std_dev_with_nan_included = series_with_nan.std(skipna=False) #This will result in NaN if any NaNs present.

print(f"Standard Deviation (NaNs skipped): {std_dev_with_nan}")

print(f"Standard Deviation (NaNs included): {std_dev_with_nan_included}")