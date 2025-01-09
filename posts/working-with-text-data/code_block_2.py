import nltk
nltk.download('punkt') # Download necessary resource

text = "This is a sentence. This is another sentence!"
tokens = nltk.word_tokenize(text)
print(f"Tokens: {tokens}")