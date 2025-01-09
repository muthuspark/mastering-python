import numpy as np

arr = np.array([1, 5, 2, 8, 3, 9, 4, 7, 6])
np.clip(arr, 3, 7, out=arr) #Modifies arr directly.
print(f"In-place clipped array: {arr}")