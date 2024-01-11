#!/usr/bin/python3
'''
This script sends a request to the provided URL and displays the response body.
'''

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    if response.status_code >= 400:
        print('Error code:', response.status_code)
    else:
        print(response.text)
