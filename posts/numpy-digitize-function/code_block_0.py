import numpy as np

scores = np.array([60, 75, 82, 90, 55, 88, 70, 95, 85])
bins = np.array([60, 70, 80, 90, 100])  # Bin edges for grades F, D, C, B, A

grade_indices = np.digitize(scores, bins)
print(grade_indices)  # Output: [1 2 3 4 1 4 2 5 3]