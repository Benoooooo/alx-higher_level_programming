#!/usr/bin/python3
'''
This script fetches the status from the provided URL using the urllib package.
'''

import urllib.request as request


if __name__ == "__main__":

    url = "https://alx-intranet.hbtn.io/status"
    with request.urlopen(url) as response:
        result = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(result)))
        print("\t- content: {}".format(result))
        print("\t- utf8 content: {}".format(result.decode("utf-8")))
