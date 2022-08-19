#!/usr/bin/python3
"""
api github connection
"""
if __name__ == "__main__":
    from requests.auth import HTTPBasicAuth
    import requests
    import sys

    usr = sys.argv[1]
    passwd = sys.argv[2]

    req = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(usr, passwd))

    try:
        data = req.json()
        print(data.get('id'))
    except ValueError:
        print("Not a valid JSON")
