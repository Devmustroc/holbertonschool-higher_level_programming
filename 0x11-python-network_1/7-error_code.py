#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of response
"""

import requests
from sys import argv

if __name__ == "__main__":
    link = requests.get(argv[1])
    if link.status_code >= 400:
        print("Error code: {}".format(link.status_code))
    else:
        print(link.text)
