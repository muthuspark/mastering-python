import requests

response = requests.get("https://www.example.com")

print(f"Status code: {response.status_code}")

if response.status_code == 200:
    content = response.text
    print(f"Website content (snippet): {content[:100]}...") #Print only the first 100 characters