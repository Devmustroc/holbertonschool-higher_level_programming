#!/usr/bin/python3

'''Send a POST request'''

from requests import post
from sys import argv

if __name__ == "__main__":

    if len(sys.argv) == 1:
        obj = {'q': ""}
    else:
        obj = {'q': sys.argv[1]}
    r = requests.post('http://0.0.0.0:5000/search_user', obj)

    try:
        dict = r.json()
        if len(dict) == 0:
            print("No result")
        else:
            print("[{}] {}".format(dict['id'], dict['name']))
    except ValueError:
        print("Not a valid JSON")
