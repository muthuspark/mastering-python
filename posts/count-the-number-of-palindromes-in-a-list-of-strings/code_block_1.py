def is_palindrome(text):
    processed_text = ''.join(c for c in text.lower() if c.isalnum())
    return processed_text == processed_text[::-1]

def count_palindromes_functional(string_list):
    return sum(1 for s in string_list if is_palindrome(s))

strings = ["racecar", "hello", "level", "World", "deified", "Racecar!"]
palindrome_count = count_palindromes_functional(strings)
print(f"Number of palindromes: {palindrome_count}") # Output: 3
