def reverse_words_method3(sentence):
  """Reverses the order of words in a sentence using a loop.

  Args:
    sentence: The input sentence as a string.

  Returns:
    The sentence with words reversed as a string.
  """
  words = sentence.split()
  reversed_words = []
  for i in range(len(words) - 1, -1, -1):
    reversed_words.append(words[i])
  return " ".join(reversed_words)

sentence = "Yet another example"
reversed_sentence = reverse_words_method3(sentence)
print(f"Original sentence: {sentence}")
print(f"Reversed sentence: {reversed_sentence}")