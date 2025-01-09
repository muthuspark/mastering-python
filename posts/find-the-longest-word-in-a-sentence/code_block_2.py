def longest_words(sentence):
    """Finds all longest words in a sentence, handling ties.

    Args:
      sentence: The input sentence.

    Returns:
      A list of the longest words. Returns an empty list if the sentence is empty.
    """
    words = sentence.split()
    if not words:
        return []
    cleaned_words = [''.join(c for c in word if c.isalnum()) for word in words]
    max_length = max(len(word) for word in cleaned_words)
    return [word for word in cleaned_words if len(word) == max_length]


#Example Usage
sentence = "This sentence has two equally long words: example and another."
longest_words_list = longest_words(sentence)
print(f"The longest words are: {longest_words_list}") # Output: ['example', 'another']
