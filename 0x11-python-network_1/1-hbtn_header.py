#!/usr/bin/env python3
"""
     sends a request to the URL and displays the value of the
     X-Request-Id variable found in the header of the response.
"""
import urllib.request as req
from sys import argv

if __name__ == "__main__":
    link = req.Request(argv[1])
    with req.urlopen(link) as req:
        print(req.headers.get('X-Request-Id'))
