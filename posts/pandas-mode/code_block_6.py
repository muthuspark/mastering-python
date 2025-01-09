empty_series = pd.Series([], dtype='int64')
mode_empty = empty_series.mode()
print(f"Mode of an empty series: {mode_empty}")