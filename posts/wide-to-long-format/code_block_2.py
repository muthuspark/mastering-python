import pandas as pd
import janitor


df_long3 = df_wide2.pivot_longer(
    index=['Student', 'Test'], names_to='Subject', values_to='Score'
)
print(df_long3)
