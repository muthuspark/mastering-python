stacked_df = df2.stack()
print(stacked_df)

unstacked_df = stacked_df.unstack()
print(unstacked_df)
