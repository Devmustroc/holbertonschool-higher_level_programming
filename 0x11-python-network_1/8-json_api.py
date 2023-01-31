#!/usr/bin/python3
"""
Send a POST request
"""
import requests as req  # import requests module
from sys import argv

if __name__ == "__main__":  # if file is executed
    url = 'http://0.0.0.0:5000/search_user' # set url to
    q = argv[1] if len(argv) > 1 else ""  # set q to argv[1] if len(argv) > 1 else ""
    res = req.post(url, data={'q': q})  # set res to req.post(url, data={'q': q})
    try: # try
        res_dic = res.json()  # set res_dic to res.json()
        if res_dic == {}:  # if res_dic is empty
            print("No result")  # print No result
        else:  # if res_dic is not empty
            print("[{}] {}".format(res_dic.get('id'), res_dic.get('name')))  # print id & name
    except ValueError:  # if ValueError
        print("Not a valid JSON") # print Not a valid JSON
