data = np.array([1, 2, 2, 3, 3, 3])
mode_result = stats.mode(data)
print(mode_result)
print("Mode:", mode_result.mode[0])