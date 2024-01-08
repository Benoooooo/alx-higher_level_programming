#!/usr/bin/python3
'''
Write a Python script that takes in a URL, sends a request
'''

import urllib.request as request
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    with request.urlopen(url) as response:

        res = response.getheader('X-Request-Id')

        print(res)
