import mmap
import numpy as np
import os

filename = "my_numpy_array.dat"

#Create a sample NumPy array
array = np.arange(1000000, dtype=np.int32).reshape(1000,1000)
with open(filename, "wb") as f:
    array.tofile(f)

try:
    with open(filename, "r+b") as f:
        mm = mmap.mmap(f.fileno(), 0)
        mapped_array = np.frombuffer(mm, dtype=np.int32).reshape(1000, 1000)
        #Now you can perform operations directly on mapped_array
        print(mapped_array[0,0]) #Access a single element
        mapped_array[0,0] = 42 #Modify a single element
        mm.close()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if os.path.exists(filename):
        os.remove(filename)
