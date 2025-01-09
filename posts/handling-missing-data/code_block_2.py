df_mean_imputed = df.fillna(df.mean())
print(df_mean_imputed)

df_median_imputed = df.fillna(df.median())
print(df_median_imputed)

df_mode_imputed = df.fillna(df.mode().iloc[0]) #iloc[0] to select first row of mode
print(df_mode_imputed)