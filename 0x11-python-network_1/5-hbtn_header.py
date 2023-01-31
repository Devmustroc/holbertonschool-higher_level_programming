#!/usr/bin/python3
"""_summary_
    """
import requests as req  # import requests module
from sys import argv  # import argv from sys

if __name__ == "__main__":  # if file is executed
    link = req.get(argv[1])  # set link to argv[1]
    print(link.headers.get('X-Request-Id'))  # print X-Request-Id
