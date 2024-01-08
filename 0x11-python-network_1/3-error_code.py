#!/usr/bin/python3
'''
python script that takes in a URL, sends a request to the URL and
displays the body of the response (decode in utf-8)
'''

import urllib.request
import sys
from urllib.error import URLError, HTTPError

if __name__ == "__main__":
    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        body = response.read()
        decoded_body = body.decode('utf-8')

    try:
        res = urllib.request.urlopen(decoded_body)
    except HTTPError as e:
        print('Thes server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print("result successful")

