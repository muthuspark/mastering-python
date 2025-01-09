def find_nth_term(a, r, n):
  """
  Calculates the nth term of a geometric sequence.

  Args:
    a: The first term of the sequence.
    r: The common ratio.
    n: The desired term number (n >= 1).

  Returns:
    The nth term of the geometric sequence.  Returns an error message if n is less than 1.

  """
  if n < 1:
    return "Error: n must be greater than or equal to 1"
  return a * (r ** (n - 1))

first_term = 2
common_ratio = 3
term_number = 5

fifth_term = find_nth_term(first_term, common_ratio, term_number)
print(f"The 5th term of the sequence is: {fifth_term}") # Output: 162


first_term = 5
common_ratio = 2
term_number = 0
zero_term = find_nth_term(first_term, common_ratio, term_number) #handles invalid input
print(zero_term) #Output: Error: n must be greater than or equal to 1
