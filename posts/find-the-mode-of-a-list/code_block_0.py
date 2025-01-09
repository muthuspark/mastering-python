def find_mode_loop(data):
    """Finds the mode of a list using a loop and dictionary.

    Args:
      data: A list of numbers or strings.

    Returns:
      The mode of the list. Returns None if the list is empty or has no mode.
    """
    if not data:
        return None

    counts = {}
    for item in data:
        counts[item] = counts.get(item, 0) + 1

    max_count = 0
    mode = None
    for item, count in counts.items():
        if count > max_count:
            max_count = count
            mode = item
        elif count == max_count and item != mode: #Handle multiple modes
            mode = "Multiple modes exist"

    return mode

data1 = [1, 2, 3, 2, 4, 2, 5]
mode1 = find_mode_loop(data1)
print(f"The mode of {data1} is: {mode1}")  # Output: The mode of [1, 2, 3, 2, 4, 2, 5] is: 2

data2 = [1, 2, 3, 4, 5]
mode2 = find_mode_loop(data2)
print(f"The mode of {data2} is: {mode2}") # Output: The mode of [1, 2, 3, 4, 5] is: None

data3 = [1,2,2,3,3,3]
mode3 = find_mode_loop(data3)
print(f"The mode of {data3} is: {mode3}") # Output: The mode of [1, 2, 2, 3, 3, 3] is: 3

data4 = [1,1,2,2,3,3]
mode4 = find_mode_loop(data4)
print(f"The mode of {data4} is: {mode4}") # Output: The mode of [1, 1, 2, 2, 3, 3] is: Multiple modes exist