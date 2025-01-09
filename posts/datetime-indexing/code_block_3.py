df_utc = df.tz_localize('UTC')

df_est = df_utc.tz_convert('US/Eastern')
print(df_est)