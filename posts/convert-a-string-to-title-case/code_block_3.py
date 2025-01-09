import re

def custom_titlecase(string):
    words = re.findall(r'\b\w+\b', string.lower()) #Find all words
    exceptions = ["a", "an", "the", "and", "but", "or", "nor", "as", "at", "by", "for", "in", "of", "on", "to", "with"]
    titlecased_words = [word.capitalize() if word not in exceptions else word for word in words]
    return " ".join(titlecased_words)


string = "this is a sample string with ARTICLES and CONJUNCTIONS"
title_case_string = custom_titlecase(string)
print(title_case_string) # Output: This is a sample string with Articles and Conjunctions
