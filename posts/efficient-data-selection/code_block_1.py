arr = np.array([10, 20, 30, 40, 50, 60])
indices = np.array([0, 2, 4])
selected_elements = arr[indices] #Selects elements at indices 0, 2, and 4
print(selected_elements) # Output: [10 30 50]

row_indices = np.array([0,1])
col_indices = np.array([1,2])
two_d_arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
selected_sub_array = two_d_arr[row_indices[:,None], col_indices]
print(selected_sub_array) # Output: [[2 3] [5 6]]
