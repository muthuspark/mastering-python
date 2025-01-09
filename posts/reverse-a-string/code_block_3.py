def reverse_string_recursive(s):
  if len(s) == 0:
    return s
  else:
    return reverse_string_recursive(s[1:]) + s[0]

string = "example"
reversed_string = reverse_string_recursive(string)
print(reversed_string) # Output: elpmaxe