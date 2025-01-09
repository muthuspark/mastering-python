data = np.array(['apple', 'banana', 'apple', 'orange', 'banana', 'banana'])
mode_result = stats.mode(data)
print(mode_result)
print("Mode:", mode_result.mode[0])