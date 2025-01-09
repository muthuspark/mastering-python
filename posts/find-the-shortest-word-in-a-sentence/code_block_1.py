def find_shortest_word_min(sentence):
    words = sentence.lower().split()
    shortest_word = min(words, key=len)
    return shortest_word

sentence = "This is a sample sentence with varying word lengths."
shortest = find_shortest_word_min(sentence)
print(f"The shortest word is: {shortest}") # Output: The shortest word is: a