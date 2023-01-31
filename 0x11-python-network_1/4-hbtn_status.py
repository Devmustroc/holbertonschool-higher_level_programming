#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""

import requests  # import requests module

if __name__ == "__main__":  # if file is executed
    link = requests.get("https://intranet.hbtn.io/status")  # set link to url
    print("Body response:")  # print response
    print("\t- type: {}".format(type(link.text)))  # print type
    print("\t- content: {}".format(link.text))  # print content
