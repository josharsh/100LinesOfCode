import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def generate_short_url(self, long_url):        
        hash_object = hashlib.md5(long_url.encode())
        short_url = hash_object.hexdigest()[:8]  
        return short_url

    def shorten_url(self, long_url):
        if long_url in self.url_map:
            return self.url_map[long_url]
        else:
            short_url = self.generate_short_url(long_url)
            self.url_map[long_url] = short_url
            return short_url

    def expand_url(self, short_url):
        for long_url, url_hash in self.url_map.items():
            if url_hash == short_url:
                return long_url
        return "Short URL not found"

if __name__ == "__main__":
    shortener = URLShortener()
    long_url = "https://www.example.com/this/is/a/long/url"
    
  
    short_url = shortener.shorten_url(long_url)
    print("Shortened URL:", short_url)
    
 
    original_url = shortener.expand_url(short_url)
    print("Original URL:", original_url)
