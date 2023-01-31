#!/usr/bin/python3
"""
request and sys
"""
import requests as req  # import requests module
from sys import argv  # import argv from sys

if __name__ == "__main__":  # if file is executed
    lk = req.get(argv[1])  # set link to argv[1]
    if lk.status_code >= 400:  # if status code is greater than or equal to 400
        print("Error code: {}".format(lk.status_code))  # print error code
    else:  # if status code is less than 400
        print(lk.text)  # print text
