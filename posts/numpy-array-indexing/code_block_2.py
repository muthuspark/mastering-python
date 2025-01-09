bool_idx = arr_1d > 20
print(arr_1d[bool_idx])  # Output: [30 40 50]

bool_idx_2d = arr_2d % 2 == 0
print(arr_2d[bool_idx_2d]) # Output: [2 4 6 8] (Note: it flattens the array)