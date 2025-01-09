import numpy as np

single_value = 10
natural_log = np.log(single_value)
print(f"The natural logarithm of {single_value} is: {natural_log}")

array = np.array([1, 10, 100, 1000])
natural_logs_array = np.log(array)
print(f"The natural logarithms of the array are: {natural_logs_array}")

#Handling potential errors (log of zero or negative numbers)
try:
    np.log(0)
except ValueError as e:
    print(f"Error: {e}") #This will print an error message about log of non-positive numbers.
try:
    np.log([-1,1])
except ValueError as e:
    print(f"Error: {e}") #This will print an error message about log of non-positive numbers.
