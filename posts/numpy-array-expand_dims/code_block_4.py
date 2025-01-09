single_image = np.random.rand(28,28)
reshaped_image = single_image[np.newaxis, ...] # adds a new axis at the beginning.  ... represents all other axes.
print(reshaped_image.shape)