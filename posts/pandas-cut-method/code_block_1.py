custom_bins = [0, 25, 50, 75, 100]  # Define custom bin edges
bins_custom = pd.cut(data, bins=custom_bins)
print("\nData with custom bins:\n", bins_custom)