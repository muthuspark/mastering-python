import re

def find_shortest_word_regex(sentence):
    words = re.findall(r'\b\w+\b', sentence.lower()) #Find all words ignoring punctuation
    return min(words, key=len) if words else "" #Handle empty sentences

sentence = "This, is. a; sample-sentence! with varying word lengths."
shortest = find_shortest_word_regex(sentence)
print(f"The shortest word is: {shortest}") # Output: The shortest word is: a
