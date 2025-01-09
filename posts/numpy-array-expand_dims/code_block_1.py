row_vector = np.expand_dims(pixel_value, axis=0)
print(row_vector.shape)  # Output: (1,)

column_vector = np.expand_dims(pixel_value, axis=1)
print(column_vector.shape)  # Output: (1, 1)