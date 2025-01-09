def find_shortest_word(sentence):
    words = sentence.lower().split()  # Convert to lowercase and split into words
    shortest_word = words[0]  # Initialize with the first word

    for word in words:
        if len(word) < len(shortest_word):
            shortest_word = word

    return shortest_word


sentence = "This is a sample sentence with varying word lengths."
shortest = find_shortest_word(sentence)
print(f"The shortest word is: {shortest}") # Output: The shortest word is: a
