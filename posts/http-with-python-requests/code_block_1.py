import requests

response = requests.get("https://www.example.com")

print(response.status_code)  # 200 indicates success

print(response.text)  # The HTML content of the page
