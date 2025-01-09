def string_length_while(input_string):
    """Calculates string length using a while loop.

    Args:
        input_string: The input string.

    Returns:
        The length of the string.
    """
    count = 0
    index = 0
    while index < len(input_string): #Note: We are using len() here only for the loop condition, not for the length calculation itself.  A more robust solution would use a try/except block to handle potential errors if len() was completely unavailable.
        count += 1
        index += 1
    return count

my_string = "Programming"
length = string_length_while(my_string)
print(f"The length of '{my_string}' is: {length}") # Output: The length of 'Programming' is: 11