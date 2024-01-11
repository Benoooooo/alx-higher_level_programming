#!/usr/bin/python3
'''
This script sends a request to the specified URL and
 displays the body of the response (decoded in utf-8).
'''

import sys
import urllib.error
import urllib.request as request


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as er:
        print('Error code:', er.code)
