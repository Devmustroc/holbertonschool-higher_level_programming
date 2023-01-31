#!/usr/bin/python3
"""
takes in a URL and an email & sends a POST request to the passed URL with the
email as a parameter & displays the body of the response
"""
import urllib.request as res
import urllib.parse as ps
from sys import argv

if __name__ == "__main__":  # if file is executed
    email = argv[2]     # set email to argv[2]
    pData = ps.urlencode({'email': email}).encode('utf-8')   # encode email
    link = res.Request(argv[1], pData)  # set link to argv[1] & pData
    with res.urlopen(link) as result:  # open link
        print(result.read().decode('utf-8'))  # print result
