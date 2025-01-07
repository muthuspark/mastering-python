import os
import random
import re
import sys
import time
from datetime import datetime, timedelta

import google.generativeai as genai

articles = """
Python Variables
Data Types in Python
Strings in Python
Numbers in Python
Booleans in Python
Type Conversion
Python Input/Output
Python Comments
Python Indentation
Operators in Python
Arithmetic Operators
Comparison Operators
Logical Operators
Assignment Operators
Bitwise Operators
Membership Operators
Identity Operators
Python Conditional Statements
If Statement
If-Else Statement
Nested If-Else
Elif Statement
Python Loops
While Loop
For Loop
Break Statement
Continue Statement
Pass Statement
Python Lists
List Operations
List Slicing
List Methods
List Comprehensions
Python Tuples
Tuple Operations
Tuple Methods
Python Sets
Set Operations
Set Methods
Python Dictionaries
Dictionary Operations
Dictionary Methods
Python Functions
Function Arguments
Default Arguments
Keyword Arguments
Arbitrary Arguments
Lambda Functions
Python Modules
Importing Modules
Standard Python Modules
Creating Your Own Modules
Python Packages
Python Scope
Python Global and Local Variables
Python Recursion
Python Exceptions
Try-Except Block
Finally Block
Raising Exceptions
Python File Handling
Opening Files
Reading Files
Writing to Files
Appending to Files
Closing Files
Python Directories
Working with OS Module
Python Date and Time
Python Math Functions
Python Random Module
Python Regular Expressions
Python Object-Oriented Programming
Python Classes
Creating Objects
Class Variables
Class Methods
Inheritance in Python
Method Overriding
Polymorphism in Python
Python Encapsulation
Python Abstraction
Python Iterators
Python Generators
Python Decorators
Python Closures
Python Context Managers
Python Virtual Environments
Installing Third-Party Libraries
Python PIP
Python Debugging
Python Unit Testing
Python Logging
Python Performance Optimization
Python Best Practices
"""

genai.configure(api_key="AIzaSyAKVnHY4B7kn41M5xotIuQucoAvPsWkqcg")

model = genai.GenerativeModel("gemini-1.5-flash")
ROOT_ARTICLE_PATH = "posts"


# Function to generate a random date
def random_date(start, end):
    delta = end - start
    random_days = random.randint(0, delta.days)
    return start + timedelta(days=random_days)


def add_random_date(file_path):
    # Define a random date range (e.g., within the next year)
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    random_generated_date = random_date(start_date, end_date).strftime('%m/%d/%Y')

    # Read the file contents
    with open(file_path, 'r') as file:
        content = file.readlines()

    if 'date:' in content[2]:
        print("date inserted already so skip")
        return

    # Modify the content by adding the random date
    for i, line in enumerate(content):
        if line.startswith("title:"):
            # After finding the title line, add the date
            content.insert(i + 1, f'date: "{random_generated_date}"\n')
            break
        
    # Write the updated content back to the file
    with open(file_path, 'w') as file:
        file.writelines(content)

    print(f"Random date added: {random_generated_date}")


def gemini_send_message_response_as_txt(message):
    print(message)
    chat = model.start_chat(history=[])
    text = chat.send_message(message).text
    return text


def write_article(post_title):
    """
    Writes an article to a blog post with a slugified name.

    Args:
      post_title: The title of the blog post.

    Returns:
      None
    """

    slugified_folder_name = re.sub(r'[^a-zA-Z0-9_-]', '',
                                   post_title.lower().replace(' ', '-')).strip('-')

    folder_path = os.path.join(ROOT_ARTICLE_PATH, slugified_folder_name)
    os.makedirs(folder_path, exist_ok=True)

    index_file_path = os.path.join(folder_path, 'index.qmd')
    if os.path.exists(index_file_path):
        print(f"Article already exists: {folder_path}")
        add_random_date(index_file_path)
        return False

    article = gemini_send_message_response_as_txt(
        f"Write a blog post about the {post_title} in python with code examples. Write SEO friendly article in markdown format. Do not generate meta description or keywords. Do no write conclusion")

    with open(index_file_path, 'w') as f:
        f.write(f"""---
title: "{post_title}"
categories: [ basic ]
---

{article}
""")

        return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a post title as an argument.")
        # sys.exit(1)

    for article in articles.split('\n'):
        if len(article.strip()) == 0:
            continue
        if write_article(article):
            time.sleep(3)

    # add dates if missing to all articles
    all_articles = [os.path.join(dp, f) for dp, dn, filenames in os.walk(ROOT_ARTICLE_PATH) for f in filenames if
                    os.path.splitext(f)[1] == '.qmd']
    for article_path in all_articles:
        add_random_date(article_path)
