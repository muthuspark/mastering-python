import pandas as pd

data = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
mode_value = data.mode()
print(f"The mode of the series is: {mode_value}")