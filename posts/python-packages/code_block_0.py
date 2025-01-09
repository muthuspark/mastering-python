import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr + 2)  # Add 2 to each element
print(arr * 2)  # Multiply each element by 2
print(np.mean(arr))  # Calculate the mean
print(np.std(arr)) # Calculate the standard deviation

arr2d = np.array([[1, 2], [3, 4]])
print(arr2d.shape) #Get the shape of the array
print(arr2d.transpose()) #transpose the array