#!/usr/bin/python3
'''
This script retrieves the value of the X-Request-Id variable
from the header of the response.
'''

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
