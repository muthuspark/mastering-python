import requests

files = {'file': open('my_file.txt', 'rb')}
response = requests.post("https://httpbin.org/post", files=files)
print(response.json())