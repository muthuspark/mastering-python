import threading
import time
import requests

def io_bound_task(url):
    response = requests.get(url)
    return response.text
