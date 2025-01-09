import numpy as np

crosstab_mean = pd.crosstab(df['Gender'], df['Purchase'], values=df['AgeGroup'], aggfunc=np.mean)
print(crosstab_mean)
