arr5 = np.array([[1, 2], [3, 4]])
arr6 = np.array([10, 20, 30])

try:
    result = arr5 + arr6 # This will raise a ValueError
    print(result)
except ValueError as e:
    print(f"Error: {e}") # Output: Error: operands could not be broadcast together with shapes (2,2) (3,) 