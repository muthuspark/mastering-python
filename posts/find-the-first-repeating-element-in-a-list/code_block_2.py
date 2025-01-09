def find_first_repeating_element_nested(data):
    """
    Finds the first repeating element in a list using nested loops.

    Args:
      data: A list of elements.

    Returns:
      The first repeating element, or None if no repeating element is found.
    """
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return data[i]
    return None

#Example Usage
my_list = [1, 2, 3, 4, 2, 5, 6, 1]
first_repeating = find_first_repeating_element_nested(my_list)
print(f"The first repeating element is: {first_repeating}")  # Output: The first repeating element is: 2

my_list2 = [1,2,3,4,5]
first_repeating2 = find_first_repeating_element_nested(my_list2)
print(f"The first repeating element is: {first_repeating2}") # Output: The first repeating element is: None