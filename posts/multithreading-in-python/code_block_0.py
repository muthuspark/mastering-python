import threading
import time
import requests

def download_file(url):
    print(f"Downloading {url}...")
    response = requests.get(url)
    response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
    with open(url.split('/')[-1], 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {url}")

urls = [
    "https://www.w3.org/TR/PNG/iso_8859-1.txt",
    "https://www.w3.org/TR/PNG/iso_8859-1.txt",
    "https://www.w3.org/TR/PNG/iso_8859-1.txt"
]

threads = []
start_time = time.time()
for url in urls:
    thread = threading.Thread(target=download_file, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()
print(f"Total download time: {end_time - start_time:.2f} seconds")
