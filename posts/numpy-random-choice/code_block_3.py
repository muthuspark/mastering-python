my_array = np.array(['X', 'Y', 'Z'])
probabilities = np.array([0.6, 0.3, 0.1]) # X has a 60% chance of selection, Y 30%, Z 10%
weighted_sample = np.random.choice(my_array, size=2, p=probabilities)
print(f"Weighted random samples: {weighted_sample}")