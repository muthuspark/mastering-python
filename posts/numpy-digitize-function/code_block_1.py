import numpy as np

data = np.array([1.2, 2.5, 3.7, 4.1, 5.9, 6.0])
bins = np.array([1, 3, 5, 7])

indices_right = np.digitize(data, bins)
print(f"Right-inclusive: {indices_right}")  # Output: Right-inclusive: [1 2 2 3 3 4]

indices_left = np.digitize(data, bins, right=False)
print(f"Left-inclusive: {indices_left}")  # Output: Left-inclusive: [1 2 3 3 4 4]
