import requests

try:
    response = requests.get("https://www.example.com")
    response.raise_for_status() # Raises an exception for bad status codes (4xx or 5xx)
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")