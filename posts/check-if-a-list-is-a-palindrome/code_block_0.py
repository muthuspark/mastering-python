def is_palindrome_slicing(list_):
  """Checks if a list is a palindrome using slicing.

  Args:
    list_: The input list.

  Returns:
    True if the list is a palindrome, False otherwise.
  """
  return list_ == list_[::-1]

my_list = [1, 2, 3, 2, 1]
print(f"Is {my_list} a palindrome? {is_palindrome_slicing(my_list)}") # Output: True

my_list = [1, 2, 3, 4, 5]
print(f"Is {my_list} a palindrome? {is_palindrome_slicing(my_list)}") # Output: False