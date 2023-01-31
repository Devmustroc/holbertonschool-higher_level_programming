#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of respons
"""

from urllib import error, request  # import error & request modules
from sys import argv  # import argv from sys

if __name__ == "__main__":  # if file is executed
    url = request.Request(argv[1])  # set url to argv[1]

    try:  # try to open url
        with request.urlopen(url) as result:      # open url
            print(result.read().decode('utf-8'))  # print result
    except error.HTTPError as err:                # if error
        print("Error code: {}".format(err.code))  # print error code
