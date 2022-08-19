#!/usr/bin/pyhton3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests as req
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) > 1 else ""
    res = req.post(url, data={'q': q})
    try:
        dic_resu = res.json()
        if dic_resu == {}:
            print("No result")
        else:
            print("[{}] {}".format(dic_resu.get('id'), dic_resu.get('name')))
    except:
        print("Not a valid JSON")
