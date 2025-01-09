def count_palindromes_comprehension(string_list):
  return sum(1 for s in string_list if is_palindrome(s)) #Reusing is_palindrome function for clarity


strings = ["racecar", "hello", "level", "World", "deified", "Racecar!"]
palindrome_count = count_palindromes_comprehension(strings)
print(f"Number of palindromes: {palindrome_count}") # Output: 3