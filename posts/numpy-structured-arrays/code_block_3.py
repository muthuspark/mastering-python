student_dtype = np.dtype([('name', 'U20'), ('grades', ('i4', 3))]) #grades is an array of 3 integers
students2 = np.zeros(2, dtype=student_dtype)

students2[0] = ('David', np.array([90,85,92]))
students2[1] = ('Eva', np.array([88,95,80]))

print(students2)
print(students2['grades'][:,0]) #access first grade for all students