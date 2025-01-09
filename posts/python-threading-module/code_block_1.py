import threading
import time
import requests

def fetch_url(url):
  response = requests.get(url)
  return response.status_code

urls = [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.wikipedia.org"
]

def threaded_fetch():
  threads = []
  for url in urls:
    thread = threading.Thread(target=fetch_url, args=(url,))
    threads.append(thread)
    thread.start()

  for thread in threads:
    thread.join()

start_time = time.time()
threaded_fetch()
end_time = time.time()
print(f"Threaded execution time: {end_time - start_time:.2f} seconds")


start_time = time.time()
for url in urls:
    fetch_url(url)
end_time = time.time()
print(f"Sequential execution time: {end_time - start_time:.2f} seconds")