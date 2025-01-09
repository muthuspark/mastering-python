import requests

params = {'param1': 'value1', 'param2': 'value2'}
response = requests.get("https://httpbin.org/get", params=params)
print(response.json()) #httpbin.org returns the parameters as json