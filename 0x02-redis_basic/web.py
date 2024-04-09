#!/usr/bin/env python3
""" implements a get_page function
"""
import redis
import requests

count = 0
cache = redis.Redis()


def get_page(url: str) -> str:
    """Obtains the HTML content of a particular URL and returns it.
    Tracks how many times the URL was accessed and store this
    count in a Redis cache.
    """
    cache.set(f"cached:{url}", count)
    response = requests.get(url)
    cache.incr(f"count:{url}")
    cache.setex(f"count:{url}", 10, cache.get(f"cached:{url}"))
    return response.text
