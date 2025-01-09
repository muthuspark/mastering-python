def is_palindrome_recursive(list_):
    """Checks if a list is a palindrome using recursion.

    Args:
        list_: The input list.

    Returns:
        True if the list is a palindrome, False otherwise.
    """
    if len(list_) <= 1:
        return True
    if list_[0] != list_[-1]:
        return False
    return is_palindrome_recursive(list_[1:-1])

my_list = [1, 2, 3, 2, 1]
print(f"Is {my_list} a palindrome? {is_palindrome_recursive(my_list)}") # Output: True

my_list = [1, 2, 3, 4, 5]
print(f"Is {my_list} a palindrome? {is_palindrome_recursive(my_list)}") # Output: False