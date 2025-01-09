from collections import Counter

def find_first_non_repeating_counter(data):
    """
    Finds the first non-repeating element using collections.Counter.

    Args:
        data: A list of elements.

    Returns:
        The first non-repeating element, or None if all elements repeat.
    """
    counts = Counter(data)
    for item in data:
        if counts[item] == 1:
            return item
    return None

#Example Usage
my_list = [10, 20, 30, 20, 10, 50, 40, 50]
first_non_repeating = find_first_non_repeating_counter(my_list)
print(f"The first non-repeating element is: {first_non_repeating}") # Output: 30

my_list2 = [1,1,2,2,3,3]
first_non_repeating2 = find_first_non_repeating_counter(my_list2)
print(f"The first non-repeating element is: {first_non_repeating2}") # Output: None