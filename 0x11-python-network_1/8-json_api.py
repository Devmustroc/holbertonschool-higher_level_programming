#!/usr/bin/python3
"""
Send a POST request
"""
import requests as req
from sys import argv

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) > 1 else ""
    res = req.post(url, data={'q': q})
    try:
        res_dic = res.json()
        if res_dic == {}:
            print("No result")
        else:
            print("[{}] {}".format(res_dic.get('id'), res_dic.get('name')))
    except:
        print("Not a valid JSON")
