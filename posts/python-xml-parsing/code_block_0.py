import xml.etree.ElementTree as ET

xml_data = """
<bookstore>
  <book category="cooking">
    <title lang="en">Everyday Italian</title>
    <author>Giada De Laurentiis</author>
    <year>2005</year>
    <price>30.00</price>
  </book>
  <book category="children">
    <title lang="en">Harry Potter</title>
    <author>J K. Rowling</author>
    <year>2005</year>
    <price>29.99</price>
  </book>
</bookstore>
"""

root = ET.fromstring(xml_data) # Parse XML string

for book in root.findall('book'):
    title = book.find('title').text
    author = book.find('author').text
    print(f"Title: {title}, Author: {author}")

#Accessing Attributes
for book in root.findall('book'):
    category = book.get('category')
    print(f"Category: {category}")
