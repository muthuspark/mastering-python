sorted_indices = np.argsort(data[:, 1].astype(int)) #Convert to integer for numerical sorting
sorted_data = data[sorted_indices]
print(sorted_data)