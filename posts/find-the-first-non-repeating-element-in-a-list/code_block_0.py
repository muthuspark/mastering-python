def find_first_non_repeating_brute_force(data):
    """
    Finds the first non-repeating element using nested loops.

    Args:
        data: A list of elements.

    Returns:
        The first non-repeating element, or None if all elements repeat.
    """
    for i, item in enumerate(data):
        is_repeating = False
        for j, other_item in enumerate(data):
            if i != j and item == other_item:
                is_repeating = True
                break
        if not is_repeating:
            return item
    return None

my_list = [10, 20, 30, 20, 10, 50, 40, 50]
first_non_repeating = find_first_non_repeating_brute_force(my_list)
print(f"The first non-repeating element is: {first_non_repeating}") # Output: 30

my_list2 = [1,1,2,2,3,3]
first_non_repeating2 = find_first_non_repeating_brute_force(my_list2)
print(f"The first non-repeating element is: {first_non_repeating2}") # Output: None
