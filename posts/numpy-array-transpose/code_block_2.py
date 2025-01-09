import numpy as np

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

transposed_arr = np.transpose(arr, (1, 0, 2)) #Swaps axes 0 and 1


print("Original Array:\n", arr)
print("\nTransposed Array:\n", transposed_arr)