import numpy as np
import numpy.ma as ma

data = np.array([1, 2, 3, 4, 5])
mask = np.array([False, True, False, False, True])
masked_array = ma.masked_array(data, mask)
print(masked_array)