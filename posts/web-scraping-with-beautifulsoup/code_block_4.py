title = soup.select_one("title").text.strip()
print(f"Title: {title}")

links = soup.select('a[href^="/about"]')
for link in links:
  print(link['href'])

product_names = soup.select('.product-name')
for product in product_names:
    print(product.text.strip())