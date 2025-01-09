import pandas as pd

dates = pd.to_datetime(['2024-10-26 09:00:00', '2024-10-26 10:00:00', '2024-10-26 11:00:00',
                       '2024-10-26 12:00:00', '2024-10-27 09:00:00'])
temperatures = [20, 22, 25, 23, 21]
df = pd.DataFrame({'Temperature': temperatures}, index=dates)
print(df)