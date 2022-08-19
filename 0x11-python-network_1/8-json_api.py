#!/usr/bin/python3
'''
Send a POST request
'''
from os import link
from requests import post
from sys import argv

if __name__ == "__main__":

    q = ""
    if len(argv) > 1:
        q = argv[1]
    lk = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        out = lk.json()
    except:
        print("Not a valid JSON")
    else:
        if out:
            print("[{}] {}".format(out['id'], out['name']))
        else:
            print("No result")
