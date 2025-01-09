import pandas as pd

#stacked_df =  df.set_index(['Category', 'Subcategory']).stack()
unstacked_df = stacked_df.unstack()

print("\nUnstacked DataFrame:\n", unstacked_df)

#Unstacking a specific level
unstacked_level0_df = stacked_df.unstack(level=0) #unstacking the Category level
print("\nUnstacked DataFrame(level 0):\n", unstacked_level0_df)

