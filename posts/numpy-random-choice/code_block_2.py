my_array = np.array(['A', 'B', 'C', 'D', 'E'])
samples = np.random.choice(my_array, size=3, replace=False)
print(f"Three random samples (without replacement): {samples}")

#This will raise a ValueError
#samples = np.random.choice(my_array, size=6, replace=False) 