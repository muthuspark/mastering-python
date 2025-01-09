def longest_palindrome_expand_around_center(s):
    n = len(s)
    if n < 2:
        return s
    start = 0
    max_len = 1
    for i in range(n):
        # Odd length palindromes
        l, r = i, i
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1
        # Even length palindromes
        l, r = i, i + 1
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1
    return s[start:start + max_len]

string = "cbbd"
result = longest_palindrome_expand_around_center(string)
print(f"The longest palindromic substring of '{string}' is: {result}") # Output: bb