def find_nth_term(a, d, n):
  """
  Calculates the nth term of an arithmetic sequence.

  Args:
    a: The first term of the sequence.
    d: The common difference.
    n: The position of the term to find.

  Returns:
    The nth term of the arithmetic sequence.  Returns an error message if n is less than 1.

  """
  if n < 1:
    return "Error: n must be a positive integer."
  return a + (n - 1) * d


first_term = 2
common_difference = 3
term_position = 5

fifth_term = find_nth_term(first_term, common_difference, term_position)
print(f"The 5th term of the sequence is: {fifth_term}") #Output: The 5th term of the sequence is: 14


first_term = 10
common_difference = -2
term_position = 8

eighth_term = find_nth_term(first_term, common_difference, term_position)
print(f"The 8th term of the sequence is: {eighth_term}") #Output: The 8th term of the sequence is: -4

invalid_term = find_nth_term(5,2,0)
print(invalid_term) #Output: Error: n must be a positive integer.