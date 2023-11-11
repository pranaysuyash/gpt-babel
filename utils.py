from urllib.parse import urlparse

def valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

# Additional utility functions can be added as needed, such as for caching and rate limiting.
