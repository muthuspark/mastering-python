import numpy as np

arr = np.array([1.234, 2.567, 3.987, -1.5])

rounded_arr = np.around(arr)  # Rounds to nearest integer
print(f"Rounded to nearest integer: {rounded_arr}")

rounded_arr_2 = np.around(arr, 2)  # Rounds to 2 decimal places
print(f"Rounded to 2 decimal places: {rounded_arr_2}")


rounded_arr_negative = np.around(arr, decimals = -1) #Rounds to nearest 10
print(f"Rounded to nearest 10: {rounded_arr_negative}")
