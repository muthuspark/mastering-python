import re

sentence = "This, is a sentence. With; punctuation!"
words = re.findall(r'\b\w+\b', sentence.lower()) #finds all words, ignoring case
word_count = len(words)
print(f"The sentence contains {word_count} words.")
