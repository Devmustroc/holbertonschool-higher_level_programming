#!/usr/bin/python3
"""
    script that fetches url
"""
import urllib.request as req

if __name__ == "__main__":
    with req.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print("Body response:")
        print(f"\t- type: {type(html)}")
        print(f"\t- content: {html}")
        print(f"\t- utf-8 content: {html.decode('utf-8')}")
