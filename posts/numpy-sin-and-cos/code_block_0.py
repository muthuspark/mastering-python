import numpy as np

angle_rad = np.pi / 4  # 45 degrees in radians
sine_value = np.sin(angle_rad)
print(f"Sine of {angle_rad} radians: {sine_value}")


angles_rad = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
sines = np.sin(angles_rad)
print(f"Sines of angles: {sines}")

#Example using degrees
degrees = np.array([0, 30, 45, 60, 90])
radians = np.deg2rad(degrees)
sines_degrees = np.sin(radians)
print(f"Sines of angles in degrees: {sines_degrees}")