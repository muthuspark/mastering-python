import numpy as np

original_array = np.array([1, 2, 3, 4, 5])

np.random.shuffle(original_array)

print("Shuffled Array (in-place):", original_array)