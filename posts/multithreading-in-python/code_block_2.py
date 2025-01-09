import concurrent.futures
import time
import requests


def download_file(url):
    # ... (same download_file function as above) ...

urls = [
    # ... (same list of URLs as above) ...
]

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = executor.map(download_file, urls)

for result in results:
    pass #Handle results if needed.
