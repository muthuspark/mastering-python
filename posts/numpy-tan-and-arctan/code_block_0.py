import numpy as np

angle_rad = np.pi / 4  # 45 degrees in radians
tangent = np.tan(angle_rad)
print(f"The tangent of {angle_rad} radians is: {tangent}")

angles_rad = np.array([0, np.pi/2, np.pi])
tangents = np.tan(angles_rad)
print(f"Tangents of angles: {tangents}") # Note: you'll get an inf for pi/2

#Handling potential errors
angles_rad = np.array([0, np.pi/2, np.pi])

try:
    tangents = np.tan(angles_rad)
    print(f"Tangents of angles: {tangents}")
except RuntimeWarning as e:
    print(f"Error calculating tangent: {e}")
