import numpy as np

x = np.array([[1, 2, 3]])  # Shape (1, 3)
y = np.squeeze(x)         # Shape (3,)
print(f"Original array x shape: {x.shape}")
print(f"Squeezed array y shape: {y.shape}")

#Example 2: Removing multiple singleton dimensions
z = np.array([[[1]]])      #Shape (1,1,1)
w = np.squeeze(z)        #Shape () - a scalar
print(f"Original array z shape: {z.shape}")
print(f"Squeezed array w shape: {w.shape}")

a = np.array([1, 2, 3])  # Shape (3,)
b = np.squeeze(a)         # Shape (3,) - No change
print(f"Original array a shape: {a.shape}")
print(f"Squeezed array b shape: {b.shape}")


#Example 4: Specifying axis to squeeze
c = np.array([[[1,2],[3,4]]]) #Shape (1,2,2)
d = np.squeeze(c, axis=0) #Shape (2,2) - squeezes along axis 0
print(f"Original array c shape: {c.shape}")
print(f"Squeezed array d shape: {d.shape}")

e = np.squeeze(c, axis=1) #This will raise an error, as axis 1 is not a singleton dimension.