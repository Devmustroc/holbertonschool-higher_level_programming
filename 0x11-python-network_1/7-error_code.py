#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of response
"""
import requests as req
from sys import argv

if __name__ == "__main__":
    lk = req.get(argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(lk.status_code))
    else:
        print(lk.text)
