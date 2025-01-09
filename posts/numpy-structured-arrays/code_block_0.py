import numpy as np

student_dtype = np.dtype([('name', 'U20'), ('age', int), ('gpa', float)])
students = np.zeros(3, dtype=student_dtype)  # Create an array of 3 students