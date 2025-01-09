def are_anagrams_dict_improved(str1, str2):
  str1 = ''.join(c for c in str1.lower() if c.isalnum())
  str2 = ''.join(c for c in str2.lower() if c.isalnum())
  # ...rest of the function remains the same...