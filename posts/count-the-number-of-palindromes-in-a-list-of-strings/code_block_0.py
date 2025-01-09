def count_palindromes_basic(string_list):
    count = 0
    for s in string_list:
        processed_string = ''.join(c for c in s.lower() if c.isalnum()) #Removes punctuation and makes lowercase
        if processed_string == processed_string[::-1]:
            count += 1
    return count

strings = ["racecar", "hello", "level", "World", "deified", "Racecar!"]
palindrome_count = count_palindromes_basic(strings)
print(f"Number of palindromes: {palindrome_count}") # Output: 3