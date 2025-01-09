data = np.array([1, 3, 5, 2, 4])
out_array = np.zeros(1) # Pre-allocate the output array
np.median(data, out=out_array)
print(f"Median using out parameter: {out_array}") # Output: Median using out parameter: [3.]
