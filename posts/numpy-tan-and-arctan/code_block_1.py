import numpy as np

tangent_value = 1
angle_rad = np.arctan(tangent_value)
print(f"The arctangent of {tangent_value} is: {angle_rad} radians")

tangent_values = np.array([0, 1, -1])
angles_rad = np.arctan(tangent_values)
print(f"Arctangents of values: {angles_rad} radians")

#Using arctan2 for a more robust solution
x_values = np.array([1, 1, -1, -1])
y_values = np.array([1, -1, 1, -1])
angles_rad = np.arctan2(y_values, x_values)
print(f"Arctangents using arctan2: {angles_rad} radians")
