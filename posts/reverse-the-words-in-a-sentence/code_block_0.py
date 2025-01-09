def reverse_words_method1(sentence):
  """Reverses the order of words in a sentence using split() and reversed().

  Args:
    sentence: The input sentence as a string.

  Returns:
    The sentence with words reversed as a string.
  """
  words = sentence.split()
  reversed_words = list(reversed(words))  # Convert reversed object to list
  return " ".join(reversed_words)

sentence = "This is a sample sentence"
reversed_sentence = reverse_words_method1(sentence)
print(f"Original sentence: {sentence}")
print(f"Reversed sentence: {reversed_sentence}")