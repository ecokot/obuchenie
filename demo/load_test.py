import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    """Один поток делает один запрос"""
    urllib.request.urlopen(url)

def main_test():
    url = sys.argv[1]  # URL из командной строки
    n_requests = 10

    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=10) as pool:
        list(pool.map(fetch, [url] * n_requests))

    elapsed = time.perf_counter() - start
    print(f"Total time: {elapsed:.2f}s")

if __name__ == "__main__":
    main_test()