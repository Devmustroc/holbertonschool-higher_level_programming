#!/usr/bin/python3
"""_summary_
    """
import requests as req
from sys import argv

if __name__ == "__main__":
    link = req.get(argv[1])
    print(link.headers.get('X-Request-Id'))
