#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""
import urllib.request as req  # import request module
from sys import argv # import argv from sys

if __name__ == "__main__":  # if file is executed
    url = req.Request(argv[1])  # set url to argv[1]
    with req.urlopen(url) as res:  # open url
        print(res.headers.get('X-Request-Id'))  # print X-Request-Id
