def longest_word_basic(sentence):
  """Finds the longest word in a sentence using basic iteration.

  Args:
    sentence: The input sentence as a string.

  Returns:
    The longest word in the sentence.  Returns an empty string if the sentence is empty.
  """
  words = sentence.split()
  if not words:
    return ""
  longest = ""
  for word in words:
    # Remove punctuation for more accurate results.
    word = ''.join(c for c in word if c.isalnum())
    if len(word) > len(longest):
      longest = word
  return longest

#Example usage
sentence = "This is a sample sentence with some punctuation!"
longest = longest_word_basic(sentence)
print(f"The longest word is: {longest}") # Output: sentence