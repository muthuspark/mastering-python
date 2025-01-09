def find_first_repeating_element_set(data):
    """
    Finds the first repeating element in a list using a set.

    Args:
      data: A list of elements.

    Returns:
      The first repeating element, or None if no repeating element is found.
    """
    seen = set()
    for element in data:
        if element in seen:
            return element
        seen.add(element)
    return None


#Example Usage
my_list = [1, 2, 3, 4, 2, 5, 6, 1]
first_repeating = find_first_repeating_element_set(my_list)
print(f"The first repeating element is: {first_repeating}")  # Output: The first repeating element is: 2

my_list2 = [1,2,3,4,5]
first_repeating2 = find_first_repeating_element_set(my_list2)
print(f"The first repeating element is: {first_repeating2}") # Output: The first repeating element is: None