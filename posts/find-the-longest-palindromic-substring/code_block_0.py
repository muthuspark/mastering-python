def longest_palindrome_brute_force(s):
    n = len(s)
    longest_palindrome = ""
    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

string = "bananas"
result = longest_palindrome_brute_force(string)
print(f"The longest palindromic substring of '{string}' is: {result}") #Output: anana