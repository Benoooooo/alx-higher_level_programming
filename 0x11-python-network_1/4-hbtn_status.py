#!/usr/bin/python3
'''
This script fetches the status from the provided URL usingthe requests package.
'''

import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    res = requests.get(url)
    print('Body response:')
    print("\t- type: {}".format(type(res.text)))
    print("\t- utf8 content: {}".format(res.text))
