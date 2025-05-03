import requests
import time

class WebpageLoadTimer:
    def __init__(self, url):
        self.url = url
        self.load_time = None

    def measure_load_time(self):
        try:
            start_time = time.time()
            response = requests.get(self.url)
            end_time = time.time()
            self.load_time = end_time - start_time
            return self.load_time
        except requests.exceptions.RequestException as e:
            print(f"Error accessing {self.url}: {e}")
            return None

    def __str__(self):
        if self.load_time is not None:
            return f"{self.url} loaded in {self.load_time:.3f} seconds."
        return f"{self.url} has not been measured yet."


if __name__ == "__main__":
    websites = [
        "https://www.google.com",
        "https://www.ynet.co.il",
        "https://www.imdb.com",
        "https://www.wikipedia.org"
    ]

    for site in websites:
        timer = WebpageLoadTimer(site)
        timer.measure_load_time()
        print(timer)
