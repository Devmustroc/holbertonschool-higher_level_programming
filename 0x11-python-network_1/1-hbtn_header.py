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


#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL with the
email as a parameter, and displays the body of the response
"""
import urllib.request as req
import urllib.parse as parse
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    data = parse.urlencode({'email': email}).encode('utf-8')
    url = req.Request(argv[1], data)
    with req.urlopen(url) as res:
        print(res.read().decode('utf-8'))