def reverse_words_method2(sentence):
  """Reverses the order of words in a sentence using slicing.

  Args:
    sentence: The input sentence as a string.

  Returns:
    The sentence with words reversed as a string.
  """
  words = sentence.split()
  return " ".join(words[::-1])

sentence = "Another example sentence"
reversed_sentence = reverse_words_method2(sentence)
print(f"Original sentence: {sentence}")
print(f"Reversed sentence: {reversed_sentence}")