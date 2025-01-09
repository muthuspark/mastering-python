import numpy as np

x = np.arange(0, 3, 1)  # x-coordinates
y = np.arange(0, 4, 1)  # y-coordinates

xv, yv = np.meshgrid(x, y)

print("x-coordinates:\n", xv)
print("\ny-coordinates:\n", yv)