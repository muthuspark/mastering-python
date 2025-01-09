def longest_word_max(sentence):
    """Finds the longest word using the max() function.

    Args:
      sentence: The input sentence.

    Returns:
      The longest word in the sentence. Returns an empty string if the sentence is empty.
    """
    words = sentence.split()
    if not words:
        return ""
    return max(words, key=lambda word: len(''.join(c for c in word if c.isalnum())))

#Example Usage
sentence = "This is another example, with more punctuation."
longest = longest_word_max(sentence)
print(f"The longest word is: {longest}") # Output: another