import requests

url = "https://www.example.com"  # Replace with your target URL
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
else:
    print(f"Error fetching URL: {response.status_code}")