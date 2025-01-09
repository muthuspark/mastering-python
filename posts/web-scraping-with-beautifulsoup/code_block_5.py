base_url = "https://www.example.com/page-"
for i in range(1, 11): # Scrape pages 1 to 10
    url = f"{base_url}{i}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    # ... your data extraction logic here ...