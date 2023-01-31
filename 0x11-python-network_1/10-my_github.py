#!/usr/bin/python3
"""
api github connection
"""
from requests.auth import HTTPBasicAuth  # import HTTPBasicAuth from requests.auth
import requests  # import requests module
import sys  # import sys module

if __name__ == "__main__":  # if file is executed

    usr = sys.argv[1]  # set usr to argv[1]
    passwd = sys.argv[2]    # set passwd to argv[2]

    req = requests.get(
        'https://api.github.com/user',
        auth=HTTPBasicAuth(usr, passwd)
    )   # set req to requests.get('https://api.github.com/user', auth=HTTPBasicAuth(usr, passwd))

    try:   # try
        data = req.json()  # set data to req.json()
        print(data.get('id'))   # print id
    except ValueError:  # if ValueError
        print("Not a valid JSON")  # print Not a valid JSON
