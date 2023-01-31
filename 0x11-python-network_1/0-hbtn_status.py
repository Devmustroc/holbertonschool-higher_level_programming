#!/usr/bin/python3
"""
    script that fetches url
"""
import urllib.request as req  # import request module

if __name__ == "__main__":  # if file is executed
    with req.urlopen('https://intranet.hbtn.io/status') as res: # open url
        html = res.read() # read response
        print("Body response:") # print response
        print("\t- type: {}".format(type(html))) # print type
        print("\t- content: {}".format(html)) # print content
        print("\t- utf8 content: {}".format(html.decode('utf-8'))) # print utf8
