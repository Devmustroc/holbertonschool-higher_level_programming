#!/usr/bin/python3
"""
    takes in a URL and an email, sends a POST request to the passed URL with the
    email as a parameter, and displays the body of the response
"""
import urllib.request as res
import urllib.parse as ps
from sys import argv

if __name__ == "__main__":
    email = argv[2]
    pData = ps.urlencode({'email': email}).encode('utf-8')
    link = res.Request(argv[1], pData)
    with res.urlopen(link) as result:
        print(result.read().decode('utf-8'))
