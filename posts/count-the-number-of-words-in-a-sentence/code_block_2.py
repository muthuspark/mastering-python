import nltk
nltk.download('punkt') # Download Punkt Sentence Tokenizer if you haven't already

from nltk.tokenize import word_tokenize

sentence = "This is a sentence with some special characters like -- and ---."
words = word_tokenize(sentence)
word_count = len(words)
print(f"The sentence contains {word_count} words.")