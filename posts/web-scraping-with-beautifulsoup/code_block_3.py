paragraphs = soup.find_all("p")
for p in paragraphs:
    print(p.text.strip())  # .text extracts text, .strip() removes whitespace