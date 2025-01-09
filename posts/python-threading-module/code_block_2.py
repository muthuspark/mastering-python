import concurrent.futures
import requests

urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org"
]

def fetch_url(url):
  response = requests.get(url)
  return url, response.status_code


with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
  future_to_url = {executor.submit(fetch_url, url): url for url in urls}
  for future in concurrent.futures.as_completed(future_to_url):
    url = future_to_url[future]
    try:
      url, status = future.result()
      print(f"URL: {url}, Status: {status}")
    except Exception as exc:
      print(f"{url} generated an exception: {exc}")
