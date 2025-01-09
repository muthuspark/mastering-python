def find_shortest_word_comprehension(sentence):
    words = sentence.lower().split()
    return min(words, key=len)


sentence = "This is a sample sentence with varying word lengths."
shortest = find_shortest_word_comprehension(sentence)
print(f"The shortest word is: {shortest}") # Output: The shortest word is: a