from concurrent.futures import ThreadPoolExecutor
import time
from random import randrange
import requests

# Function to send GET request
def send_get_request(url):
    try:
        response = requests.get(url)
        print(f"Response from {url}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

while True:
    time.sleep(randrange(10, 30))

    # List of URLs to send GET requests to
    urls = ['http://localhost:9092'] * randrange(1, 10)

    # Use ThreadPoolExecutor to send requests in parallel
    with ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(send_get_request, urls)