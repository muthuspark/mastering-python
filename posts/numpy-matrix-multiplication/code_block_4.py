import numpy as np
import matplotlib.pyplot as plt

rotation_matrix = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                            [np.sin(np.pi/4), np.cos(np.pi/4)]])

point = np.array([1, 0])

rotated_point = rotation_matrix @ point

#Plot the points
plt.plot([0,point[0]],[0,point[1]],label="Original Point")
plt.plot([0,rotated_point[0]],[0,rotated_point[1]],label="Rotated Point")
plt.legend()
plt.show()