import requests

headers = {'User-Agent': 'My custom User-Agent'}
response = requests.get("https://www.example.com", headers=headers)
print(response.status_code)