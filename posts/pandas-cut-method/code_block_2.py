labels = ['Low', 'Medium', 'High', 'Very High']
bins_labeled = pd.cut(data, bins=4, labels=labels)
print("\nData with labeled bins:\n", bins_labeled)

bins_labeled_custom = pd.cut(data, bins=custom_bins, labels=labels)
print("\nData with custom labeled bins:\n", bins_labeled_custom)
