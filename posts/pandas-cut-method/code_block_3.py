bins_right_closed = pd.cut(data, bins=4, right=True) # default
print("\nRight-closed bins:\n",bins_right_closed)

bins_left_closed = pd.cut(data, bins=4, right=False) #Left closed
print("\nLeft-closed bins:\n",bins_left_closed)


#Example with include_lowest
bins_include_lowest = pd.cut(data, bins=custom_bins, include_lowest=True, right=False)
print("\nBins including lowest:\n", bins_include_lowest)