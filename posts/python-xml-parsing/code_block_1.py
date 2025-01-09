from lxml import etree

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

root = etree.fromstring(xml_data)

for book in root.xpath('//book'): #Using XPath for powerful querying
    title = book.xpath('.//title/text()')[0]
    author = book.xpath('.//author/text()')[0]
    print(f"Title: {title}, Author: {author}")

for book in root.xpath('//book'):
    category = book.get('category')
    print(f"Category: {category}")