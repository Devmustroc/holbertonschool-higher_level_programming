#!/usr/bin/python3
"""
request and sys
"""
import requests as req
from sys import argv

if __name__ == "__main__":
    lk = req.get(argv[1])
    if lk.status_code >= 400:
        print("Error code: {}".format(lk.status_code))
    else:
        print(lk.text)
