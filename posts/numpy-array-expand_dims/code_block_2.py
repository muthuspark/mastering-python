image = np.array([[1, 2], [3, 4]])
print(image.shape)  # Output: (2, 2)

batched_image = np.expand_dims(image, axis=0)
print(batched_image.shape)  # Output: (1, 2, 2)