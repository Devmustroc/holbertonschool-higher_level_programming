#!/usr/bin/python3
"""
takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and finally displays the body of the response.
"""

import requests  # import requests module
from sys import argv  # import argv from sys

if __name__ == "__main__":  # if file is executed
    link = requests.post(argv[1], data={"email": argv[2]})  # set link to argv[1] & argv[2]
    print(link.text)  # print link
