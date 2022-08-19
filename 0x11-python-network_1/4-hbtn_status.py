#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    link = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(link.text)))
    print("\t- content: {}".format(link.text))
