#!/usr/bin/python3
'''
This script retrieves the value of the X-Request-Id variable
from the header of the response using the requests package.
'''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')
    print(x_request_id)
