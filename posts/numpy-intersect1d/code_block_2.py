array7 = np.array([1, 2, 3, 4, 5])
array8 = np.array([3, 5, 6, 7, 8])

intersection = np.intersect1d(array7, array8, assume_unique=True)
print(intersection) # Output: [3 5]