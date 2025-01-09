from scipy import interpolate
import numpy as np

x = np.array([0, 1, 2])
y = np.array([1, 3, 2])

f = interpolate.interp1d(x, y)

xnew = np.array([0.5, 1.5])
ynew = f(xnew)
print(f"Interpolated values: {ynew}")
