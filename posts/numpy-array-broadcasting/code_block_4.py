arr7 = np.array([1,2,3])
arr8 = np.array([[4],[5],[6]])

result = arr7[:, np.newaxis] + arr8 #Adding a new axis to arr7 allows for broadcasting

print(result) # Output: [[5 6 7] [6 7 8] [7 8 9]]