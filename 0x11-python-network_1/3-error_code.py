#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of respons
"""

from urllib import error, request
from sys import argv

if __name__ == "__main__":
    url = request.Request(argv[1])

    try:
        with request.urlopen(url) as result:
            print(result.read().decode('utf-8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
