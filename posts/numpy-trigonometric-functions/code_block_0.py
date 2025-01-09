import numpy as np

angles_rad = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])

sine_values = np.sin(angles_rad)
cosine_values = np.cos(angles_rad)
tangent_values = np.tan(angles_rad)

print("Angles (radians):", angles_rad)
print("Sine values:", sine_values)
print("Cosine values:", cosine_values)
print("Tangent values:", tangent_values)


y = 1
x = 1
angle_degrees = np.degrees(np.arctan2(y, x))
print(f"The angle (degrees) using arctan2 for y={y}, x={x} is: {angle_degrees}")

#Example with hypotenuse calculation
x = 3
y = 4
hypotenuse = np.hypot(x,y)
print(f"The hypotenuse of a triangle with legs {x} and {y} is: {hypotenuse}")

#Convert Degrees to Radians and vice versa

angles_deg = np.array([0, 90, 180, 270, 360])
angles_rad_converted = np.radians(angles_deg)
angles_deg_converted = np.degrees(angles_rad)

print("Angles (degrees):", angles_deg)
print("Angles (radians, converted):", angles_rad_converted)
print("Angles (degrees, converted from radians):", angles_deg_converted)