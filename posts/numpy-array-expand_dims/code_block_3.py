single_image = np.random.rand(28, 28)
reshaped_image = np.expand_dims(single_image, axis=0)
print(reshaped_image.shape) #Output: (1, 28, 28)