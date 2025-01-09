original_dict = {"x": 10, "y": [1, 2]}
copied_dict = original_dict.copy()
copied_dict["x"] = 20
print(original_dict)  # Output: {'x': 10, 'y': [1, 2]}
print(copied_dict)  # Output: {'x': 20, 'y': [1, 2]}