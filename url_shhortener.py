# Implement a URL shortener with the following methods:

# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.
# restore(short), which expands the shortened string into the original url. If no such shortened string exists, return null.
# Hint: What if we enter the same URL twice?
import random
class Shortener:
    def __init__(self):
        self.storage = {}
    def shorten(self, url):
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        numerical = '1234567890'
        alphanumerical = list(alpha + numerical + alpha.upper())
        if url in self.storage:
            return self.storage[url]
        # generate shortened url
        shortUrl = ''
        while len(shortUrl) < 6:
            shortUrl += random.choice(alphanumerical)
            if shortUrl in self.storage.values():
                shortUrl = ''
        self.storage[url] = shortUrl
        return shortUrl
    def restore(self, short_url):
        long_url = [l for l, s in self.storage.items() if s == short_url]
        return long_url

if __name__ == "__main__":
    URLs = ["www.facebook.com", "www.google.com", "www.facebook.com"]
    shortened_URL = []
    shortener = Shortener()
    for url in URLs:
        short_url = shortener.shorten(url)
        shortened_URL.append(short_url)
    for s_url in shortened_URL:
        print(shortener.restore(s_url))
    