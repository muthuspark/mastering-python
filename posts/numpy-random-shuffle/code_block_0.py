import numpy as np

original_array = np.array([1, 2, 3, 4, 5])
shuffled_array = np.copy(original_array)  # Create a copy
np.random.shuffle(shuffled_array)

print("Original Array:", original_array)
print("Shuffled Array:", shuffled_array)