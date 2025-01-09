def is_palindrome_loop(list_):
  """Checks if a list is a palindrome using a loop.

  Args:
    list_: The input list.

  Returns:
    True if the list is a palindrome, False otherwise.
  """
  left = 0
  right = len(list_) - 1
  while left < right:
    if list_[left] != list_[right]:
      return False
    left += 1
    right -= 1
  return True

my_list = [1, 2, 3, 2, 1]
print(f"Is {my_list} a palindrome? {is_palindrome_loop(my_list)}") # Output: True

my_list = [1, 2, 3, 4, 5]
print(f"Is {my_list} a palindrome? {is_palindrome_loop(my_list)}") # Output: False