def string_length_iterative(input_string):
  """Calculates the length of a string iteratively.

  Args:
    input_string: The string whose length needs to be determined.

  Returns:
    The length of the string as an integer.  Returns 0 for an empty string.
  """
  count = 0
  for _ in input_string:
    count += 1
  return count

my_string = "Hello, world!"
length = string_length_iterative(my_string)
print(f"The length of '{my_string}' is: {length}")  # Output: The length of 'Hello, world!' is: 13

empty_string = ""
length = string_length_iterative(empty_string)
print(f"The length of '{empty_string}' is: {length}") # Output: The length of '' is: 0