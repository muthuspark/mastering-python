import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
bool_arr = np.array([True, False, True, False, True, False])

selected_elements = arr[bool_arr]  # Selects elements where bool_arr is True
print(selected_elements)  # Output: [10 30 50]

selected_elements = arr[(arr > 20) & (arr < 50)] # Elements greater than 20 and less than 50
print(selected_elements) # Output: [30 40]