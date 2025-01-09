x = np.arange(0, 3, 1)
y = np.arange(0, 4, 1)
z = np.arange(0, 2, 1)

xv, yv, zv = np.meshgrid(x, y, z, indexing='xy')

print("Shape of 3D x-coordinate array:", xv.shape) # Output: (4, 3, 2)