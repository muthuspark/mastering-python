import requests

response = requests.get("https://api.example.com", auth=('username', 'password'))
print(response.status_code)