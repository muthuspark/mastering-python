import numpy as np

angle_rad = np.pi / 3 # 60 degrees in radians
cosine_value = np.cos(angle_rad)
print(f"Cosine of {angle_rad} radians: {cosine_value}")


angles_rad = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
cosines = np.cos(angles_rad)
print(f"Cosines of angles: {cosines}")

#Example using degrees
degrees = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(degrees)
cosines_degrees = np.cos(radians)
print(f"Cosines of angles in degrees: {cosines_degrees}")