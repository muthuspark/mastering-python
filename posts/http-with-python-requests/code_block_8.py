import requests

response = requests.get("https://www.example.com", timeout=5) # Timeout after 5 seconds
print(response.status_code)