col2_loc = df.loc[:, 'col2'] # : selects all rows
print("\n.loc for single column:\n", col2_loc)

cols_loc = df.loc[:, ['col1', 'col2']]
print("\n.loc for multiple columns:\n", cols_loc)