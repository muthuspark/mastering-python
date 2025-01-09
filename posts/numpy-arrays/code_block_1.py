zeros_array = np.zeros((2, 3))
print(zeros_array)

ones_array = np.ones((3, 3))
print(ones_array)

full_array = np.full((2, 2), 7)
print(full_array)

arange_array = np.arange(0, 10, 2) #Start, stop, step
print(arange_array)

linspace_array = np.linspace(0, 1, 5) #Start, stop, number of samples
print(linspace_array)

#Creating a 3x3 identity matrix
identity_matrix = np.identity(3)
print(identity_matrix)

#Creating an array of random numbers
random_array = np.random.rand(2,3) # 2 rows, 3 columns
print(random_array)
