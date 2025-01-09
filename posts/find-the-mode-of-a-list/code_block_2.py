from collections import Counter

def find_mode_counter(data):
    """Finds the mode of a list using collections.Counter.

    Args:
      data: A list of numbers or strings.

    Returns:
      The mode of the list. Returns None if the list is empty.  Returns "Multiple modes exist" if multiple modes exist.
    """
    if not data:
        return None

    counts = Counter(data)
    max_count = max(counts.values())
    modes = [item for item, count in counts.items() if count == max_count]

    if len(modes) > 1:
        return "Multiple modes exist"
    elif len(modes) == 0:
        return None
    else:
        return modes[0]

data1 = [1, 2, 3, 2, 4, 2, 5]
mode1 = find_mode_counter(data1)
print(f"The mode of {data1} is: {mode1}")

data2 = [1, 2, 3, 4, 5]
mode2 = find_mode_counter(data2)
print(f"The mode of {data2} is: {mode2}")

data3 = [1,2,2,3,3,3]
mode3 = find_mode_counter(data3)
print(f"The mode of {data3} is: {mode3}")

data4 = [1,1,2,2,3,3]
mode4 = find_mode_counter(data4)
print(f"The mode of {data4} is: {mode4}")